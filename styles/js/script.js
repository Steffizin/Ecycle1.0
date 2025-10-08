const map = L.map('map').setView([-23.620464473249893, -46.72967968674794], 16); // Coordenadas próximas da ETEC Abdias

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    }).addTo(map);

    const iconeVerde = L.icon({
      iconUrl: '../img/missoes/mis1.png',
      iconSize: [32, 32],
    });

    const iconeLaranja = L.icon({
      iconUrl: '../img/pontoLaranja.png',
      iconSize: [32, 32],
      className: 'orange-icon'
    });

    L.marker([-23.620014136933627, -46.731924025049615], { icon: iconeLaranja }).addTo(map)
      .bindPopup('Você está aqui!');

    L.marker([-23.621718724878775, -46.72845048246778], { icon: iconeVerde }).addTo(map)
      .bindPopup('Ponto de coleta: Escola Técnica Abdias');