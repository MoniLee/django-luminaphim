// Theme Toggle Functionality
(function() {
    const THEME_KEY = 'luminaphim-theme';
    const LIGHT_THEME = 'light-theme';
    const DARK_THEME = 'dark-theme';

    // Initialize theme on page load
    function initTheme() {
        // Check localStorage for saved theme
        const savedTheme = localStorage.getItem(THEME_KEY);
        
        // Check system preference if no saved theme
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        
        // Determine which theme to apply (default to dark)
        const themeToApply = savedTheme || (prefersDark ? LIGHT_THEME : DARK_THEME);
        
        // Apply the theme
        applyTheme(themeToApply);
    }

    // Apply theme to the body
    function applyTheme(theme) {
        const body = document.body;
        
        // Remove theme class if it exists
        body.classList.remove(LIGHT_THEME);
        
        // Add the light-theme class if switching to light mode
        if (theme === LIGHT_THEME) {
            body.classList.add(LIGHT_THEME);
        }
        
        // Save to localStorage
        localStorage.setItem(THEME_KEY, theme);
        
        // Update toggle button icons
        updateToggleIcons(theme);
    }

    // Update toggle button icon display
    function updateToggleIcons(theme) {
        const themeToggle = document.getElementById('themeToggle');
        if (!themeToggle) return;

        const lightIcon = themeToggle.querySelector('.light-icon');
        const darkIcon = themeToggle.querySelector('.dark-icon');

        if (theme === LIGHT_THEME) {
            // Light mode: show moon icon (for switching to dark)
            if (lightIcon) lightIcon.style.display = 'none';
            if (darkIcon) darkIcon.style.display = 'block';
        } else {
            // Dark mode: show sun icon (for switching to light)
            if (lightIcon) lightIcon.style.display = 'block';
            if (darkIcon) darkIcon.style.display = 'none';
        }
    }

    // Get current theme
    function getCurrentTheme() {
        return document.body.classList.contains(LIGHT_THEME) ? LIGHT_THEME : DARK_THEME;
    }

    // Toggle theme
    function toggleTheme() {
        const currentTheme = getCurrentTheme();
        const newTheme = currentTheme === LIGHT_THEME ? DARK_THEME : LIGHT_THEME;
        applyTheme(newTheme);
    }

    // Add click event listener to toggle button
    if (document.readyState === 'loading') {
        // DOM is still loading
        document.addEventListener('DOMContentLoaded', function() {
            // Initialize theme after a brief delay to ensure all DOM elements are ready
            setTimeout(initTheme, 50);

            // Add click listener to theme toggle button
            const themeToggle = document.getElementById('themeToggle');
            if (themeToggle) {
                themeToggle.addEventListener('click', toggleTheme);
            }
        });
    } else {
        // DOM is already loaded
        initTheme();
        
        const themeToggle = document.getElementById('themeToggle');
        if (themeToggle) {
            themeToggle.addEventListener('click', toggleTheme);
        }
    }

    // Listen for system theme changes
    if (window.matchMedia) {
        const darkModeQuery = window.matchMedia('(prefers-color-scheme: dark)');
        darkModeQuery.addListener((e) => {
            // Only apply system preference if no user preference is saved
            if (!localStorage.getItem(THEME_KEY)) {
                applyTheme(e.matches ? LIGHT_THEME : DARK_THEME);
            }
        });
    }

    // Expose toggle function globally for debugging
    window.toggleTheme = toggleTheme;
})();
