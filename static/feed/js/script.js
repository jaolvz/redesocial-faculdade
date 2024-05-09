window.onload = function() {
    ajustarTamanhoTexto();
  };
  
  window.onresize = function() {
    ajustarTamanhoTexto();
  };
  
  function ajustarTamanhoTexto() {
    var div = document.querySelector('.quadro_info');
    var titulos = document.getElementsByClassName('h1_info');
    var maxWidth = div.clientWidth;
   
    for (var i = 0; i < titulos.length; i++) {
        var titulo = titulos[i];
        var fontSize = 32; // Tamanho inicial da fonte
        titulo.style.fontSize = fontSize + 'px';

        while (titulo.offsetWidth > maxWidth && fontSize > 5) {
            fontSize -= 1; // Diminui o tamanho da fonte
            titulo.style.fontSize = fontSize + 'px';
    }

    }
  }