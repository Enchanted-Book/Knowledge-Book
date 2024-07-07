const getTheme = () => {
  const theme = document.documentElement.dataset.theme;
  return (theme === "light" || theme === "dark") ? theme : (
    window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  )
}

observer.observe(document.documentElement, {attributes: true, attributeFilter: ['data-theme']});
