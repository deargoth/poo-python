from classe.cp import ContaPoupanca
from classe.cc import ContaCorrente

cp = ContaPoupanca(2222, 1111, 'R$600')
cp.depositar(400)
cp.sacar(200)

cc = ContaCorrente(1231, 4341, 0, 500)
cc.sacar(300)