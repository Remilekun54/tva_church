// 1. Tailwind & Lucide Init (Immediate)
tailwind.config = {
  theme: {
    extend: {
      colors: {
        primary: "#8B1A3E",
        secondary: "#FFD700",
        accent: "#F5A623",
        brandLight: "#FFF8E1",
      },
      animation: {
        "bounce-slow": "bounce 3s infinite",
        "pulse-slow": "pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite",
      },
    },
  },
};
lucide.createIcons();
gsap.registerPlugin(ScrollTrigger);

// 2. Global Function for the "X" Button (Must be outside any blocks)
window.closeMessage = function (button) {
  const message =
    button.closest(".django-message") || button.closest(".animate-bounce-slow");
  if (message) {
    gsap.to(message, {
      opacity: 0,
      y: -20,
      duration: 0.3,
      onComplete: () => message.remove(),
    });
  }
};

// 3. Navigation & Mobile Menu
document.addEventListener("DOMContentLoaded", () => {
  const menuBtn = document.getElementById("mobile-menu-button");
  const mobileMenu = document.getElementById("mobile-menu");
  if (menuBtn && mobileMenu) {
    menuBtn.onclick = () => mobileMenu.classList.toggle("hidden");
  }

  // Auto-hide messages after 6 seconds
  setTimeout(() => {
    const alerts = document.querySelectorAll(
      ".django-message, .animate-bounce-slow"
    );
    alerts.forEach((alert) => {
      gsap.to(alert, {
        opacity: 0,
        y: -20,
        duration: 0.5,
        onComplete: () => alert.remove(),
      });
    });
  }, 6000);
});

// 4. Navbar Scroll Effect
window.addEventListener("scroll", () => {
  const nav = document.getElementById("navbar");
  if (!nav) return;
  window.scrollY > 100
    ? nav.classList.add("h-16", "shadow-2xl")
    : nav.classList.remove("h-16", "shadow-2xl");
});

// 5. Hero Carousel Logic
window.addEventListener("load", function () {
  const slides = document.querySelectorAll(".hero-slide");
  const dots = document.querySelectorAll(".dot-progress");
  let currentIndex = 0;
  if (slides.length === 0) return;

  function playSlide(index) {
    slides.forEach((slide, i) => {
      if (i === index) {
        gsap.to(slide, { opacity: 1, zIndex: 10, duration: 1 });
        const content = slide.querySelector(".slide-content");
        if (content)
          gsap.fromTo(
            content.children,
            { y: 50, opacity: 0 },
            { y: 0, opacity: 1, duration: 1, stagger: 0.2, delay: 0.5 }
          );
      } else {
        gsap.to(slide, { opacity: 0, zIndex: 0, duration: 1 });
      }
    });
    dots.forEach((dot, i) => {
      gsap.set(dot, { width: 0 });
      if (i === index)
        gsap.to(dot, { width: "100%", duration: 6, ease: "none" });
    });
  }
  playSlide(0);
  setInterval(() => {
    currentIndex = (currentIndex + 1) % slides.length;
    playSlide(currentIndex);
  }, 6000);
});
