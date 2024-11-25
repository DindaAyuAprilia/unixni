document.addEventListener('DOMContentLoaded', () => {
    const galeriSelects = document.querySelectorAll('.galeri-select'); // Semua opsi dropdown
    const galeriSections = document.querySelectorAll('.galeri-section'); // Semua galeri

    // Default: Tampilkan galeri pertama
    const defaultGaleri = document.querySelector('.galeri-section.active');
    if (defaultGaleri) {
        defaultGaleri.classList.remove('d-none');
    }

    galeriSelects.forEach((select) => {
        select.addEventListener('click', (event) => {
            event.preventDefault(); // Mencegah reload
            const galeriId = event.target.getAttribute('data-galeri-id'); // Ambil ID galeri

            // Hide all galeri sections
            galeriSections.forEach((section) => {
                section.classList.add('d-none');
                section.classList.remove('active'); // Pastikan tidak ada yang aktif
            });

            // Show the selected galeri section
            const selectedGaleri = document.getElementById(galeriId);
            if (selectedGaleri) {
                selectedGaleri.classList.remove('d-none');
                selectedGaleri.classList.add('active'); // Tandai sebagai aktif
            }
        });
    });
});
