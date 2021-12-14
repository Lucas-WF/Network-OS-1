class Form extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
      <style>
	.tabela {
	   width: 216px;
	   height: 276px;
	   margin: 0 39px 24px 0;
	   border: 1px dotted #000;
	   display: inline-block;
	   vertical-align: top;
	   padding: 5px;
 	  background-color: #fff;
	}

	h2 {
	 color: #e32020;
	}

	h4 {
	 color: black;
	}
      </style>
      <body>
	<div class="tabela" id="comp_table">
            <form action="cgi-bin/comprimento.py" method="post">
            	<h2>Comprimento:</h2>
		<h4>De:</h4>

		<input type="text" name="Comprimento">
            	<select name="comprimentos" id="medidas_comp">
               	    <option value="mm">Milímetro</option>
                    <option value="cm">Centímetro</option>
                    <option value="dm">Decímetro</option>
                    <option value="m">Metro</option>
                    <option value="dam">Decâmetro</option>
                    <option value="hm">Hectômetro</option>
                    <option value="km">Quilômetro</option>
                </select>
                <button>Enviar</button>
            </form>
	</div>
	
	<div class="tabela" id="massa_table">
        <form action="cgi-bin/massa.py" method="post">
            <h2>Massa:</h2>
	    <input type="text" name="Massa">
            <select name="massas" id="medidas_massa">
                <option value="mg">Miligrama</option>
                <option value="cg">Centigrama</option>
                <option value="dg">Decigrama</option>
                <option value="g">Grama</option>
                <option value="dag">Decagrama</option>
                <option value="hg">Hectograma</option>
                <option value="kg">Quilograma</option>
            </select>
            <button>Enviar</button>
        </form>
	</div>
	
	<div class="tabela" id="tempo_table">
        <form action="cgi-bin/tempo.py" method="post">
            <h2>Tempo:</h2>
	    <input type="text" name="Tempo">
            <select name="tempos" id="medidas_temp">
                <option value="milisegundo">Milisegundo</option>
                <option value="segundo">Segundo</option>
                <option value="minuto">Minuto</option>
                <option value="hora">Hora</option>
                <option value="dia">Dia</option>
            </select>
            <button>Enviar</button>
        </form>
	</div>
    </body>
    `;
  }
}

customElements.define('form-component', Form);