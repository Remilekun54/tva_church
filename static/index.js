// 1. Tailwind Configuration (Extended for Glassmorphism support)
tailwind.config = {
  theme: {
    extend: {
      colors: {
        primary: "#20359A", // TVA Blue
        secondary: "#7BC62D", // TVA Green
        accent: "#4C9F28", // TVA Dark Green
        brandLight: "#F0F9FF",
        glassBase: "rgba(255, 255, 255, 0.65)",
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', "sans-serif"],
        serif: ['"Fraunces"', "serif"],
      },
      backdropBlur: {
        xs: '2px',
      },
      boxShadow: {
        'glass': '0 8px 32px 0 rgba(31, 38, 135, 0.15)',
        'glass-hover': '0 8px 32px 0 rgba(31, 38, 135, 0.25)',
      },
    },
  },
};

// 2. Initialize Icons & GSAP
lucide.createIcons();
gsap.registerPlugin(ScrollTrigger);

// 3. Global Animations & Interactions
document.addEventListener("DOMContentLoaded", () => {
    
  // A. Mobile Menu Animation (Full Screen Glass)
  const menuBtn = document.getElementById("mobile-menu-button");
  const mobileMenu = document.getElementById("mobile-menu");
  
  if (menuBtn && mobileMenu) {
    // Initial State: Hidden 
    gsap.set(mobileMenu, { y: "-100%", opacity: 0, display: "none" });

    let isMenuOpen = false;

    menuBtn.onclick = () => {
      isMenuOpen = !isMenuOpen;
      if (isMenuOpen) {
        gsap.set(mobileMenu, { display: "block" });
        gsap.to(mobileMenu, { 
            y: "0%", 
            opacity: 1, 
            duration: 0.6, 
            ease: "power3.out" 
        });
        // Stagger in links
        gsap.fromTo(mobileMenu.querySelectorAll('a'), 
            { y: 20, opacity: 0 },
            { y: 0, opacity: 1, duration: 0.4, stagger: 0.1, delay: 0.2 }
        );
      } else {
        gsap.to(mobileMenu, { 
            y: "-100%", 
            opacity: 0, 
            duration: 0.5, 
            ease: "power3.in",
            onComplete: () => gsap.set(mobileMenu, { display: "none" })
        });
      }
    };
  }

  // B. Scroll Reveal Animations (Global)
  
  // 1. Text Reveals (Slide Up)
  gsap.utils.toArray('.reveal-text').forEach(element => {
    gsap.to(element, {
      scrollTrigger: {
        trigger: element,
        start: "top 85%",
        toggleActions: "play none none reverse",
      },
      y: 0,
      opacity: 1,
      duration: 1,
      ease: "power2.out"
    });
  });

  // 2. Card Reveals (Scale In)
  gsap.utils.toArray('.glass-card, .reveal-card').forEach((element, i) => {
    gsap.to(element, {
      scrollTrigger: {
        trigger: element,
        start: "top 90%",
      },
      scale: 1,
      opacity: 1,
      duration: 0.8,
      delay: i * 0.1, // staggering handled by delay logic if grouped, simplistic here
      ease: "back.out(1.7)"
    });
  });

  // 3. Image Reveals (Unblur & Scale)
  gsap.utils.toArray('.reveal-image').forEach(element => {
    gsap.to(element, {
      scrollTrigger: {
        trigger: element,
        start: "top 80%",
      },
      filter: "blur(0px)",
      scale: 1,
      opacity: 1,
      duration: 1.5,
      ease: "power2.out"
    });
  });


  // C. Interactive Buttons (Magnetic Effect - Optional polish)
  const buttons = document.querySelectorAll('button, .btn-glass');
  buttons.forEach(btn => {
      btn.addEventListener('mousemove', (e) => {
          const rect = btn.getBoundingClientRect();
          const x = e.clientX - rect.left - rect.width / 2;
          const y = e.clientY - rect.top - rect.height / 2;
          gsap.to(btn, { x: x * 0.1, y: y * 0.1, duration: 0.2 });
      });
      btn.addEventListener('mouseleave', () => {
          gsap.to(btn, { x: 0, y: 0, duration: 0.2 });
      });
  });
});

// 4. Hero Carousel Logic (Enhanced)
window.addEventListener("load", function () {
  const slides = document.querySelectorAll(".hero-slide");
  const dots = document.querySelectorAll(".dot-progress");
  let currentIndex = 0;
  
  if (slides.length > 0) {
      function playSlide(index) {
        slides.forEach((slide, i) => {
          const content = slide.querySelector(".slide-content");
          const img = slide.querySelector("img");

          if (i === index) {
            // Active Slide
            gsap.to(slide, { opacity: 1, zIndex: 10, duration: 1.2 });
            gsap.fromTo(img, { scale: 1.1 }, { scale: 1, duration: 6, ease: "none" }); // Ken burns
            if (content) {
                gsap.fromTo(content.children, 
                    { y: 50, opacity: 0, filter: "blur(10px)" }, 
                    { y: 0, opacity: 1, filter: "blur(0px)", duration: 1, stagger: 0.15, delay: 0.5, ease: "power2.out" }
                );
            }
          } else {
            // Inactive Slide
            gsap.to(slide, { opacity: 0, zIndex: 0, duration: 1 });
          }
        });
        
        // Dots
        dots.forEach((dot, i) => {
          gsap.killTweensOf(dot);
          gsap.set(dot, { width: i === index ? "0%" : "0%" });
          if (i === index) {
              gsap.to(dot, { width: "100%", duration: 6, ease: "none" });
          }
        });
      }

      playSlide(0);
      setInterval(() => {
        currentIndex = (currentIndex + 1) % slides.length;
        playSlide(currentIndex);
      }, 6000);
  }
});
