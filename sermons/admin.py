from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
import datetime
from .models import Sermon, Book, SermonCategory, AudioBroadcast


@admin.register(SermonCategory)
class SermonCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'preacher', 'branch', 'date_preached', 'status', 'is_trending', 'is_live_recording')
    list_filter = ('category', 'status', 'branch', 'is_trending', 'is_live_recording', 'date_preached')
    search_fields = ('title', 'theme', 'series_name', 'description', 'preacher__name')
    list_editable = ('status', 'is_trending')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'category', 'theme', 'series_name', 'description', 'thumbnail')
        }),
        ('Pricing', {
            'fields': ('status', 'price')
        }),
        ('External Links', {
            'fields': ('video_url', 'audio_url')
        }),
        ('Direct Uploads', {
            'fields': ('video_file', 'audio_file')
        }),
        ('Details & Relationships', {
            'fields': ('preacher', 'branch', 'duration', 'date_preached')
        }),
        ('Visibility', {
            'fields': ('is_trending', 'is_live_recording')
        }),
    )

    def get_changeform_initial_data(self, request):
        return {'date_preached': datetime.date.today()}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'price', 'book_type', 'created_at')
    list_filter = ('status', 'book_type', 'author')
    search_fields = ('title', 'author', 'description')
    list_editable = ('status', 'price')

    fieldsets = (
        ('Book Details', {
            'fields': ('title', 'author', 'book_type', 'description', 'thumbnail', 'pages')
        }),
        ('Pricing & Access', {
            'fields': ('status', 'price', 'pdf_file', 'external_purchase_link')
        }),
    )


@admin.register(AudioBroadcast)
class AudioBroadcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'preacher', 'live_status_badge', 'stream_key_display', 'last_broadcast_end', 'created_at')
    list_filter = ('is_live',)
    readonly_fields = ('stream_key', 'obs_setup_instructions', 'last_broadcast_end', 'created_at')

    fieldsets = (
        ('📡 Broadcast Control', {
            'description': 'Toggle "Is Live" to show/hide the Listen Live player on the website.',
            'fields': ('title', 'preacher', 'is_live'),
        }),
        ('🎙️ OBS Stream Configuration (Read Only)', {
            'description': 'Use these settings in OBS Studio → Settings → Stream.',
            'fields': ('stream_key', 'obs_setup_instructions'),
            'classes': ('collapse',),
        }),
        ('🔗 HLS Playback URL', {
            'description': 'After starting your media server, paste the .m3u8 URL here so the player can tune in.',
            'fields': ('hls_stream_url',),
        }),
        ('📅 Timestamps', {
            'fields': ('last_broadcast_end', 'created_at'),
            'classes': ('collapse',),
        }),
    )

    def live_status_badge(self, obj):
        if obj.is_live:
            return format_html(
                '<span style="background:#dc2626;color:#fff;padding:3px 10px;'
                'border-radius:12px;font-weight:bold;font-size:11px;">🔴 LIVE</span>'
            )
        return format_html(
            '<span style="background:#6b7280;color:#fff;padding:3px 10px;'
            'border-radius:12px;font-size:11px;">⚫ Offline</span>'
        )
    live_status_badge.short_description = 'Status'

    def stream_key_display(self, obj):
        return format_html('<code style="font-size:11px;">{}</code>', str(obj.stream_key))
    stream_key_display.short_description = 'Stream Key'

    def obs_setup_instructions(self, obj):
        return format_html(
            '<div style="background:#1e1e2e;color:#cdd6f4;padding:16px;border-radius:8px;font-family:monospace;font-size:13px;line-height:1.8;">'
            '<strong style="color:#89b4fa;">OBS Studio Setup:</strong><br>'
            '1. Open OBS → Settings → Stream<br>'
            '2. Service: <strong style="color:#a6e3a1;">Custom</strong><br>'
            '3. Server: <strong style="color:#f9e2af;">rtmp://your-media-server.com/live</strong><br>'
            '4. Stream Key: <strong style="color:#f38ba8;">{}</strong><br><br>'
            '<strong style="color:#89b4fa;">Then paste your HLS URL:</strong><br>'
            'e.g. <strong style="color:#f9e2af;">https://your-server.com/live/{}/index.m3u8</strong>'
            '</div>',
            str(obj.stream_key),
            str(obj.stream_key),
        )
    obs_setup_instructions.short_description = 'OBS Setup Guide'