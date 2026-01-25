// 1. Tailwind Configuration (Extended for Glassmorphism support)
// Note: tailwind.config is already defined in base.html, so this file just handles logic.

/**
 * TVA - The Vineyard Assembly 
 * Main Interactive Script
 */

// Initialize Icons
lucide.createIcons();

// 2. Global Mobile Menu Logic
window.toggleMenu = function() {
    const mobileMenu = document.getElementById("mobile-menu");
    if (!mobileMenu) return;

    const isHidden = mobileMenu.classList.contains("hidden");

    if (isHidden) {
        // Show Menu
        mobileMenu.classList.remove("hidden");
        document.body.style.overflow = "hidden"; // Prevent background scrolling
        
        // GSAP Animation
        gsap.fromTo(mobileMenu, 
            { y: 50, opacity: 0 }, 
            { y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }
        );
    } else {
        // Hide Menu
        gsap.to(mobileMenu, { 
            y: 50, 
            opacity: 0, 
            duration: 0.3, 
            onComplete: () => {
                mobileMenu.classList.add("hidden");
                document.body.style.overflow = "auto"; 
            }
        });
    }
};

// 3. Mobile Accordion Logic
window.toggleAccordion = function(id) {
    const element = document.getElementById(id);
    const icon = document.getElementById('icon-' + id);
    if (!element) return;

    const isHidden = element.classList.contains('hidden');

    if (isHidden) {
        element.classList.remove('hidden');
        if(icon) icon.style.transform = 'rotate(180deg)';
        
        gsap.fromTo(element, 
            { height: 0, opacity: 0 },
            { height: "auto", opacity: 1, duration: 0.3 }
        );
    } else {
        gsap.to(element, {
            height: 0,
            opacity: 0,
            duration: 0.2,
            onComplete: () => {
                element.classList.add('hidden');
                if(icon) icon.style.transform = 'rotate(0deg)';
                // Reset inline styles from GSAP so it can be re-opened
                element.style.height = ''; 
                element.style.opacity = '';
            }
        });
    }
}

// 4. Hero Carousel & Scroll Effects
document.addEventListener("DOMContentLoaded", () => {
    
    // --- Hero Carousel Logic ---
    const slides = document.querySelectorAll(".hero-slide");
    const dots = document.querySelectorAll(".dot-progress");
    let currentIndex = 0;

    if (slides.length > 0) {
        function playSlide(index) {
            slides.forEach((slide, i) => {
                if (i === index) {
                    slide.style.opacity = "1";
                    slide.style.zIndex = "10";
                } else {
                    slide.style.opacity = "0";
                    slide.style.zIndex = "0";
                }
            });
            
            // Update dots progress indicators
            dots.forEach((dot, i) => {
                dot.style.width = i === index ? "100%" : "0%";
            });
        }

        // Initialize first slide
        playSlide(0);

        // Auto-play interval
        setInterval(() => {
            currentIndex = (currentIndex + 1) % slides.length;
            playSlide(currentIndex);
        }, 6000);
    }

    // --- Navbar Scroll Effect ---
    const navbar = document.getElementById("navbar");
    if (navbar) {
        window.addEventListener("scroll", () => {
            if (window.scrollY > 50) {
                navbar.classList.add("shadow-glass", "bg-white/80", "backdrop-blur-md", "py-2");
                navbar.classList.remove("bg-transparent", "h-24");
                navbar.classList.add("h-20");
            } else {
                navbar.classList.remove("shadow-glass", "bg-white/80", "backdrop-blur-md", "py-2");
                navbar.classList.add("bg-transparent", "h-24");
                navbar.classList.remove("h-20");
            }
        });
    }

    // --- 5. Gallery Slider Logic ---
    const track = document.getElementById("gallery-track");
    const btnPrev = document.getElementById("forcePrev");
    const btnNext = document.getElementById("forceNext");
    
    if (track && btnPrev && btnNext) {
        let scrollAmount = 0;
        const scrollStep = 340; // width of card + gap approx
        
        btnNext.addEventListener("click", () => {
            const maxScroll = track.scrollWidth - track.clientWidth;
            scrollAmount += scrollStep;
            if (scrollAmount > maxScroll) scrollAmount = 0; // Loop back
            track.style.transform = `translateX(-${scrollAmount}px)`;
        });

        btnPrev.addEventListener("click", () => {
            scrollAmount -= scrollStep;
            if (scrollAmount < 0) {
                 // Go to end
                 const maxScroll = track.scrollWidth - track.clientWidth;
                 scrollAmount = maxScroll > 0 ? maxScroll : 0; 
            }
            track.style.transform = `translateX(-${scrollAmount}px)`;
        });
    }

    // --- 6. Advanced Scroll Animations (GSAP) ---
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        // Utility function for consistent triggers
        const setupTrigger = (trigger, animationData) => {
            return {
                ...animationData,
                scrollTrigger: {
                    trigger: trigger,
                    start: "top 85%", // Start animation when top of element hits 85% of viewport
                    toggleActions: "play none none reverse" 
                }
            };
        };

        // 1. Hero Text Stagger (already handled by CSS/HTML structure usually, but let's reinforce)
        // (Skipping Hero to avoid conflict with existing carousel logic which handles opacity)

        // 2. About Section
        gsap.from(".glass-card img", setupTrigger(".glass-card", {
            x: -50, opacity: 0, duration: 1, ease: "power2.out"
        }));
        gsap.from(".lg\\:w-1\\/2 h2", setupTrigger(".lg\\:w-1\\/2 h2", {
            x: 50, opacity: 0, duration: 1, delay: 0.2
        }));

        // 3. Sermons Preview
        gsap.from("#sermons-preview .sermon-header", setupTrigger("#sermons-preview", {
            y: 30, opacity: 0, duration: 0.8
        }));
        gsap.from(".sermon-card", setupTrigger("#sermons-preview .grid", {
            y: 50, opacity: 0, duration: 0.8, stagger: 0.1
        }));

        // 4. Core Values (GOGAP / TVA Experience)
        gsap.from(".grid .group", setupTrigger(".py-32 .grid", {
            scale: 0.9, opacity: 0, duration: 0.6, stagger: 0.2, ease: "back.out(1.7)"
        }));

        // 5. Store Section
        gsap.from(".store-image", setupTrigger("#store-preview", {
            x: -50, opacity: 0, duration: 1
        }));
        gsap.from(".store-text", setupTrigger("#store-preview", {
            x: 50, opacity: 0, duration: 1
        }));

        // 6. Pastor Section
        gsap.from(".pastor-info", setupTrigger("#pastor-section", {
            x: -50, opacity: 0, duration: 1
        }));
        gsap.from(".pastor-image", setupTrigger("#pastor-section", {
            scale: 0.8, opacity: 0, duration: 1, ease: "power2.out"
        }));

        // 7. Events Section
        gsap.from(".event-card", setupTrigger("#events", {
            y: 30, opacity: 0, duration: 0.8, stagger: 0.1
        }));

        // 8. Gallery Section
        gsap.from("#gallery-track img", setupTrigger("#gallery-track", {
            x: 100, opacity: 0, duration: 0.8, stagger: 0.1
        }));

        // 9. Featured Quote
        gsap.from(".bg-primary i, .bg-primary h2", setupTrigger(".bg-primary.py-24", {
            scale: 0.9, opacity: 0, duration: 1, stagger: 0.2
        }));

        // 10. Offering Section
        gsap.from(".shadow-inner", setupTrigger(".py-24.bg-white .shadow-inner", {
            y: 50, opacity: 0, duration: 1, ease: "elastic.out(1, 0.7)"
        }));

        // 11. Contact Section
        gsap.from("#contact-preview h2, #contact-preview .space-y-8", setupTrigger("#contact-preview", {
            x: -30, opacity: 0, duration: 1, stagger: 0.2
        }));
        gsap.from("#contact-preview form", setupTrigger("#contact-preview", {
            x: 30, opacity: 0, duration: 1
        }));
    }

    // Re-run icon initialization for any dynamic elements
    lucide.createIcons();
});