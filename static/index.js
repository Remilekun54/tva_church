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

    // --- Reveal Animations on Scroll ---
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        const cards = document.querySelectorAll('.glass-card');
        cards.forEach(card => {
            gsap.fromTo(card,
                { y: 50, opacity: 0 },
                {
                    y: 0, 
                    opacity: 1, 
                    duration: 0.8,
                    scrollTrigger: {
                        trigger: card,
                        start: "top 85%",
                    }
                }
            )
        });
    }

    // Re-run icon initialization for any dynamic elements
    lucide.createIcons();
});