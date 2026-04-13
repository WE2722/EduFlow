(function () {
    const smartSearch = document.getElementById('smart-search');
    const resultsBox = document.getElementById('search-results');

    if (smartSearch && resultsBox) {
        let timerId = null;

        smartSearch.addEventListener('input', function () {
            const query = smartSearch.value.trim();
            clearTimeout(timerId);

            if (query.length < 2) {
                resultsBox.classList.add('d-none');
                resultsBox.innerHTML = '';
                return;
            }

            timerId = setTimeout(async function () {
                const response = await fetch(`/students/ajax/search/?q=${encodeURIComponent(query)}`);
                const payload = await response.json();
                const results = payload.results || [];

                if (!results.length) {
                    resultsBox.innerHTML = '<div class="list-group-item">No match found</div>';
                    resultsBox.classList.remove('d-none');
                    return;
                }

                resultsBox.innerHTML = results
                    .map((item) => `<a class="list-group-item list-group-item-action" href="/students/${item.id}/"><strong>${item.full_name}</strong><br><small>${item.email} • ${item.filiere}</small></a>`)
                    .join('');
                resultsBox.classList.remove('d-none');
            }, 250);
        });

        document.addEventListener('click', function (event) {
            if (!resultsBox.contains(event.target) && event.target !== smartSearch) {
                resultsBox.classList.add('d-none');
            }
        });
    }

    const filieresChart = document.getElementById('chart-filieres');
    if (filieresChart && typeof Chart !== 'undefined') {
        const labels = JSON.parse(filieresChart.dataset.labels || '[]');
        const values = JSON.parse(filieresChart.dataset.values || '[]');
        new Chart(filieresChart, {
            type: 'bar',
            data: {
                labels,
                datasets: [{ label: 'Students', data: values, backgroundColor: '#2563eb' }],
            },
            options: { responsive: true, plugins: { legend: { display: false } } },
        });
    }

    const statusChart = document.getElementById('chart-status');
    if (statusChart && typeof Chart !== 'undefined') {
        const labels = JSON.parse(statusChart.dataset.labels || '[]');
        const values = JSON.parse(statusChart.dataset.values || '[]');
        new Chart(statusChart, {
            type: 'doughnut',
            data: {
                labels,
                datasets: [{ data: values, backgroundColor: ['#22c55e', '#f59e0b', '#3b82f6'] }],
            },
            options: { responsive: true },
        });
    }
})();
