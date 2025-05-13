# Beecrowd - 1048 | Aumento de Salário

<div class="problem">
            <div class="description">
                <p>A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:</p>
                <br>
                <div align="center">
                    <table style="width: 500px">
                        <thead>
                            <tr>
                                <td>Salário</td>
                                <td>Percentual de Reajuste</td>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="division">
                                    <p style="text-align: center">
                                        0 - 400.00<br>
                                        400.01 - 800.00<br>
                                        800.01 - 1200.00<br>
                                        1200.01 - 2000.00<br>
                                        Acima de 2000.00
                                    </p>
                                </td>
                                <td>
                                    <p style="text-align: center">
                                        15%<br>
                                        12%<br>
                                        10%<br>
                                        7%<br>
                                        4%
                                    </p>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <p style="text-align: justify">Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.</p>
            </div>
            <h2>Entrada</h2>
            <div class="input">
                <p>A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.</p>
            </div>
            <h2>Saída</h2>
            <div class="output">
                <p>Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.</p>
            </div>
            <div class="both"></div>
            <table>
                <thead>
                    <tr>
                        <td>Exemplo de Entrada</td>
                        <td>Exemplo de Saída</td>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="division">
                            <p>400.00</p>
                        </td>
                        <td>
                            <p>
                                Novo salario: 460.00<br>
                                Reajuste ganho: 60.00<br>
                                Em percentual: 15 %
                            </p>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table>
                <tbody>
                    <tr>
                        <td class="division">
                            <p>800.01</p>
                        </td>
                        <td>
                            <p>
                                Novo salario: 880.01<br>
                                Reajuste ganho: 80.00<br>
                                Em percentual: 10 %
                            </p>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table>
                <tbody>
                    <tr>
                        <td class="division">
                            <p>2000.00</p>
                        </td>
                        <td>
                            <p>
                                Novo salario: 2140.00<br>
                                Reajuste ganho: 140.00<br>
                                Em percentual: 7 %
                            </p>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>