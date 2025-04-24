# Beecrowd - 1045 | Tipos de Triângulo

<div class="problem">
            <div class="description">
                <p>Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:<br></p>
                <ul>
                    <li>se A ≥ B+C, apresente a mensagem: <strong>NAO FORMA TRIANGULO</strong></li>
                    <li>se A<sup>2</sup> = B<sup>2</sup> + C<sup>2</sup>, apresente a mensagem: <strong>TRIANGULO RETANGULO</strong></li>
                    <li>se A<sup>2</sup> &gt; B<sup>2</sup> + C<sup>2</sup>, apresente a mensagem: <strong>TRIANGULO OBTUSANGULO</strong></li>
                    <li>se A<sup>2</sup> &lt; B<sup>2</sup> + C<sup>2</sup>, apresente a mensagem: <strong>TRIANGULO ACUTANGULO</strong></li>
                    <li>se os três lados forem iguais, apresente a mensagem: <strong>TRIANGULO EQUILATERO</strong></li>
                    <li>se apenas dois dos lados forem iguais, apresente a mensagem: <strong>TRIANGULO ISOSCELES</strong></li>
                </ul>
            </div>
            <h2>Entrada</h2>
            <div class="input">
                <p>A entrada contem três valores de ponto flutuante de dupla precisão A (0 &lt; A) , B (0 &lt; B) e C (0 &lt; C).</p>
            </div>
            <h2>Saída</h2>
            <div class="output">
                <p>Imprima todas as classificações do triângulo especificado na entrada.</p>
            </div>


|Exemplos de Entrada|Exemplos de Saída|
|--|--|
|7.0 5.0 7.0|TRIANGULO ACUTANGULO<br>TRIANGULO ISOSCELES|
|6.0 6.0 10.0|TRIANGULO OBTUSANGULO<br>TRIANGULO ISOSCELES|
|6.0 6.0 6.0|TRIANGULO ACUTANGULO<br>TRIANGULO EQUILATERO|
|5.0 7.0 2.0|NAO FORMA TRIANGULO|
|6.0 8.0 10.0|TRIANGULO RETANGULO|