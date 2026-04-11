// Theme Toggle Functionality
(function() {
  // Get the stored theme preference or default to 'dark'
  const getThemePreference = () => {
    const stored = localStorage.getItem('theme-preference');
    if (stored) {
      return stored;
    }
    // Check system preference
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  };

  // Set the theme
  const setTheme = (theme) => {
    const htmlElement = document.documentElement;
    const body = document.body;
    
    if (theme === 'light') {
      body.classList.remove('dark-mode');
      body.classList.add('light-mode');
    } else {
      body.classList.remove('light-mode');
      body.classList.add('dark-mode');
    }
    
    localStorage.setItem('theme-preference', theme);
    updateToggleButton(theme);
  };

  // Update toggle button appearance
  const updateToggleButton = (theme) => {
    const toggleBtn = document.querySelector('.theme-toggle');
    if (toggleBtn) {
      toggleBtn.classList.remove('light-mode', 'dark-mode');
      toggleBtn.classList.add(theme + '-mode');
    }
  };

  // Toggle between themes
  const toggleTheme = () => {
    const currentTheme = localStorage.getItem('theme-preference') || 'dark';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
  };

  // Initialize theme on page load
  const initTheme = () => {
    const preferredTheme = getThemePreference();
    setTheme(preferredTheme);

    // Add click event listener to toggle button
    const toggleBtn = document.querySelector('.theme-toggle');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', toggleTheme);
    }
  };

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTheme);
  } else {
    initTheme();
  }

  // Listen for system theme changes
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    // Only apply if no user preference is stored
    if (!localStorage.getItem('theme-preference')) {
      setTheme(e.matches ? 'dark' : 'light');
    }
  });
})();
