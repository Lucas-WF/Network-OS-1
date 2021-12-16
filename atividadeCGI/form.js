class Form extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
      <style>
	.tabela {
	   width: 216px;
	   height: 300px;
	   margin: 0 39px 24px 0;
	   border: 2px dotted #000;
	   display: inline-block;
	   vertical-align: top;
	   padding: 5px;
 	  background-color: #fff;
	}

  .controlador_op {
    display: block;
    width: 100%;
    height: 34px;
    padding: 6px 12px;
    font-size: 14px;
    line-height: 1.42857143;
    color: #555;
    background-color: #fff;
    background-image: none;
    border: 1px solid #003;
    border-radius: 4px;
    box-shadow: inset 0 1px 1px rgb(0 0 0 / 8%);
    transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  }

  .controlador_input{
    display: block;
    width: 88.5%;
    height: 20px;
    padding: 6px 12px;
    font-size: 14px;
    line-height: 1.42857143;
    color: #555;
    background-color: #fff;
    background-image: none;
    border: 1px solid #003;
    border-radius: 4px;
    box-shadow: inset 0 1px 1px rgb(0 0 0 / 8%);
    transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
    margin-top: 10px;
  }

  h2 {
	 color: #e32020;
   margin: 0;
	}

	h4 {
	 color: black;
	}

  button {
    margin-top: 10px;
  }
      </style>
      <body>
	<div class="tabela" id="comp_table">
            <form action="cgi-bin/comprimento.py" method="post">

            	<h2>Comprimento</h2>
              <input type="text" name="comprimento" class="controlador_input">
		          <h4>DE:</h4>

            	<select name="comprimento_p1" id="medidas_comp" class="controlador_op">
               	    <option value="mm">Milímetro</option>
                    <option value="cm">Centímetro</option>
                    <option value="dm">Decímetro</option>
                    <option value="m">Metro</option>
                    <option value="dam">Decâmetro</option>
                    <option value="hm">Hectômetro</option>
                    <option value="km">Quilômetro</option>
                </select>

              <h4>PARA:</h4>

              <select name="comprimento_p2" id="medidas_comp" class="controlador_op">
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

            <h2>Massa</h2>
            <input type="text" name="massa" class="controlador_input">
            <h4>DE:</h4>

            <select name="massa_p1" id="medidas_massa" class="controlador_op">
                <option value="mg">Miligrama</option>
                <option value="cg">Centigrama</option>
                <option value="dg">Decigrama</option>
                <option value="g">Grama</option>
                <option value="dag">Decagrama</option>
                <option value="hg">Hectograma</option>
                <option value="kg">Quilograma</option>
            </select>

            <h4>PARA:</h4>

            <select name="massa_p2" id="medidas_massa" class="controlador_op">
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
        <form action="cgi-bin/area.py" method="post">

            <h2>Área</h2>
            <input type="text" name="area" class="controlador_input">
            <h4>DE:</h4>

            <select name="area_p1" id="medidas_temp" class="controlador_op">
                <option value="mm²">Milímetro²</option>
                <option value="cm²">Centímetro²</option>
                <option value="dm²">Decímetro²</option>
                <option value="m²">Metro²</option>
                <option value="are">Are</option>
                <option value="ha">Hectare</option>
                <option value="km²">Quilômetro²</option>
            </select>

            <h4>PARA:</h4>
            
            <select name="area_p2" id="medidas_temp" class="controlador_op">
                <option value="mm²">Milímetro²</option>
                <option value="cm²">Centímetro²</option>
                <option value="dm²">Decímetro²</option>
                <option value="m²">Metro²</option>
                <option value="are">Are</option>
                <option value="ha">Hectare</option>
                <option value="km²">Quilômetro²</option>
            </select>

            <button>Enviar</button>
        </form>
	</div>
    </body>
    `;
  }
}

customElements.define('form-component', Form);