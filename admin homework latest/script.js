const toggleSwitch = document.getElementById('dark-mode-toggle');
const currentTheme = localStorage.getItem('theme');

// 브라우저 새로고침 시, 이전에 저장된 테마를 불러와 적용
if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);

    if (currentTheme === 'dark') {
        toggleSwitch.checked = true;
    }
}

// 토글 상태에 따라 테마 전환
toggleSwitch.addEventListener('change', function(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
    }
});