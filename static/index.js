// 1. Tailwind Configuration (Extended for Glassmorphism support)
// Note: tailwind.config is already defined in base.html, so this file just handles logic.

/**
 * TVA - The Vineyard Assembly 
 * Main Interactive Script
 */

// Initialize Icons
lucide.createIcons();
console.log("TVA Church: index.js loaded successfully");

// 2. Global Mobile Menu Logic
window.toggleMenu = function() {
    const mobileMenu = document.getElementById("mobile-menu");
    if (!mobileMenu) return;

    // Utilize Tailwind's 'hidden' class for toggling
    if (mobileMenu.classList.contains("hidden")) {
        mobileMenu.classList.remove("hidden");
        document.body.style.overflow = "hidden"; // Prevent background scrolling
    } else {
        mobileMenu.classList.add("hidden");
        document.body.style.overflow = "auto";
    }
};

// 3. Mobile Accordion Logic
window.toggleAccordion = function(id) {
    const element = document.getElementById(id);
    const icon = document.getElementById('icon-' + id);
    if (!element) return;

    if (element.classList.contains('hidden')) {
        element.classList.remove('hidden');
        if(icon) icon.style.transform = 'rotate(180deg)';
    } else {
        element.classList.add('hidden');
        if(icon) icon.style.transform = 'rotate(0deg)';
    }
    
    // Smooth transition can be added via CSS utility classes if needed, 
    // but for now we prioritize functionality.
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
    // --- Navbar Scroll Effect ---
    const navbar = document.getElementById("navbar");
    const navMenuList = document.getElementById("nav-menu-list");

    if (navbar) {
        const updateNavbar = () => {
             // Get all direct links and buttons in the menu
            const menuItems = navMenuList ? navMenuList.querySelectorAll("a, button") : [];

            if (window.scrollY > 50) {
                // Scrolled down: Increase navbar height, add glass effect AND Blue Bottom Border
                navbar.classList.add("shadow-glass", "bg-white/80", "backdrop-blur-md", "border-b", "border-primary");
                navbar.classList.remove("bg-transparent", "h-24");
                navbar.classList.add("h-28");

                // Also increase menu list height (by increasing padding)
                if (navMenuList) {
                    navMenuList.classList.remove("p-1");
                    navMenuList.classList.add("px-2", "py-3"); // Taller pill
                    
                    // Increase Font Size
                    menuItems.forEach(item => {
                        item.classList.remove("text-sm");
                        item.classList.add("text-base");
                    });
                }
            } else {
                // At top: Default height and transparent. Remove Blue Border.
                navbar.classList.remove("shadow-glass", "bg-white/80", "backdrop-blur-md", "h-28", "border-b", "border-primary");
                navbar.classList.add("bg-transparent", "h-24");

                // Revert menu list height
                if (navMenuList) {
                    navMenuList.classList.remove("px-2", "py-3");
                    navMenuList.classList.add("p-1"); // Default compact pill

                    // Revert Font Size
                    menuItems.forEach(item => {
                        item.classList.remove("text-base");
                        item.classList.add("text-sm");
                    });
                }
            }
        };

        // Listen for scroll events
        window.addEventListener("scroll", updateNavbar);
        
        // Run immediately on load to handle reload/restoration position
        updateNavbar();
    }

    // --- 5. Gallery Slider Logic ---
    const track = document.getElementById("gallery-track");
    const btnPrev = document.getElementById("forcePrev");
    const btnNext = document.getElementById("forceNext");
    
    if (track && btnPrev && btnNext) {
        let scrollAmount = 0;
        
        const updateSlider = () => {
            const firstImage = track.querySelector('img');
            if (!firstImage) return;

            const imageWidth = firstImage.offsetWidth;
            const gap = 24; // Corresponding to Tailwind 'gap-6' (6 * 4px)
            const scrollStep = imageWidth + gap;
            const maxScroll = track.scrollWidth - track.parentElement.clientWidth;

            btnNext.onclick = () => {
                scrollAmount += scrollStep;
                if (scrollAmount > maxScroll) {
                    scrollAmount = 0; // Seamless loop back to start
                }
                gsap.to(track, {
                    x: -scrollAmount,
                    duration: 0.6,
                    ease: "power2.inOut"
                });
            };

            btnPrev.onclick = () => {
                scrollAmount -= scrollStep;
                if (scrollAmount < 0) {
                    scrollAmount = maxScroll > 0 ? maxScroll : 0; // Go to end
                }
                gsap.to(track, {
                    x: -scrollAmount,
                    duration: 0.6,
                    ease: "power2.inOut"
                });
            };
        };

        // Initialize and handle resize
        window.addEventListener('load', updateSlider);
        window.addEventListener('resize', updateSlider);
        updateSlider();
    }

    // --- 6. Advanced Scroll Animations (GSAP) ---
    // DISABLED TEMPORARILY: Debugging blank page issue
    if (false && typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        // Utility function for consistent triggers
        const setupTrigger = (trigger, animationData) => {
            return {
                ...animationData,
                scrollTrigger: {
                    trigger: trigger,
                    start: "top 95%", // Trigger much earlier (almost immediately when entering screen)
                    toggleActions: "play none none none" // Play once and stay visible. Do NOT reverse/hide on scroll up.
                }
            };
        };

        // 1. Hero (Skipped to preserve carousel)

        // 2. About Section
        // Note: Classes might have changed, using safe selectors
        const aboutImages = document.querySelectorAll(".glass-card img");
        if(aboutImages.length > 0) {
             gsap.from(aboutImages, setupTrigger(".glass-card", {
                x: -30, opacity: 0, duration: 0.6, ease: "power2.out"
            }));
        }
        
        const aboutText = document.querySelectorAll(".lg\\:w-1\\/2 h2");
        if(aboutText.length > 0) {
            gsap.from(aboutText, setupTrigger(".lg\\:w-1\\/2 h2", {
                x: 30, opacity: 0, duration: 0.6, delay: 0.1
            }));
        }

        // 3. Sermons Preview
        gsap.from("#sermons-preview .sermon-header", {
            scrollTrigger: {
                trigger: "#sermons-preview",
                start: "top 90%",
                toggleActions: "play none none none"
            },
            y: 30,
            opacity: 0,
            duration: 0.8
        });

        gsap.from(".sermon-card", {
            scrollTrigger: {
                trigger: "#sermons-preview .grid",
                start: "top 90%",
                toggleActions: "play none none none"
            },
            y: 30,
            opacity: 0,
            duration: 0.8,
            stagger: 0.1,
            clearProps: "all" // Important: prevents conflicts with CSS transitions after GSAP finishes
        });

        // 4. Core Values
        gsap.from(".grid .group", setupTrigger(".py-32 .grid", {
            scale: 0.95, opacity: 0, duration: 0.5, stagger: 0.1, ease: "back.out(1.2)"
        }));

        // 5. Store Section
        gsap.from(".store-image", setupTrigger("#store-preview", {
            x: -30, opacity: 0, duration: 0.8
        }));
        gsap.from(".store-text", setupTrigger("#store-preview", {
            x: 30, opacity: 0, duration: 0.8
        }));

        // 6. Pastor Section
        gsap.from(".pastor-info", setupTrigger("#pastor-section", {
            x: -30, opacity: 0, duration: 0.8
        }));
        gsap.from(".pastor-image", setupTrigger("#pastor-section", {
            scale: 0.9, opacity: 0, duration: 0.8, ease: "power2.out"
        }));

        // 7. Events Section (Removed animation to fix visibility issues)

        // 8. Gallery Section
        gsap.from("#gallery-track img", setupTrigger("#gallery-track", {
            x: 50, opacity: 0, duration: 0.6, stagger: 0.1
        }));

        // 9. Featured Quote
        gsap.from(".bg-primary i, .bg-primary h2", setupTrigger(".bg-primary.py-24", {
            scale: 0.95, opacity: 0, duration: 0.8, stagger: 0.2
        }));

        // 10. Offering Section
        gsap.from(".shadow-inner", setupTrigger(".py-24.bg-white .shadow-inner", {
            y: 30, opacity: 0, duration: 0.8
        }));

        // 11. Contact Section
        gsap.from("#contact-preview h2, #contact-preview .space-y-8", setupTrigger("#contact-preview", {
            x: -20, opacity: 0, duration: 0.8, stagger: 0.1
        }));
        gsap.from("#contact-preview form", setupTrigger("#contact-preview", {
            x: 20, opacity: 0, duration: 0.8
        }));

        // 12. Branches Section (Removed animation to fix visibility issues)
    }
    // Final refresh to catch any late-loading layouts (like images)
    window.addEventListener("load", () => {
        if (typeof ScrollTrigger !== 'undefined') {
            ScrollTrigger.refresh();
        }
    });

    // Re-run icon initialization for any dynamic elements
    lucide.createIcons();
});

// 7. Scroll to Top Logic (Robust Implementation)
document.addEventListener("DOMContentLoaded", () => {
    const scrollToTopBtn = document.getElementById("scrollToTopBtn");
    
    if (scrollToTopBtn) {
        // Show/Hide logic
        window.addEventListener("scroll", () => {
            if (window.scrollY > 400) {
                scrollToTopBtn.classList.remove("translate-y-24", "opacity-0");
            } else {
                scrollToTopBtn.classList.add("translate-y-24", "opacity-0");
            }
        });

        // Click logic attached via JS for better separation
        scrollToTopBtn.addEventListener("click", (e) => {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });
    }
    
    // Global function fallback just in case
    window.scrollToTop = function() {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    };
});

