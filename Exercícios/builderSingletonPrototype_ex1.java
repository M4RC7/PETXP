public class Nota {
	double valor;
	double desconto;
	double imposto;
	int emissao;
	int vencimento;
	String empresa;
	double valorTotal;
}

public abstract class notaBuilder {
	protected Nota nota;
	public notaBuilder {
		nota = new Nota();
	}
	public abstract void buildValor;
	public abstract void buildDesconto;
	public abstract void buildImposto;
	public abstract void buildEmissao;
	public abstract void buildVencimento;
	public abstract void buildEmpresa;
	public abstract void buildValorTotal;
	public Nota getNota() {
		return nota;
	}
}

public class minasBuilder extends notaBuilder {
	public void buildValor(){
		double x;
		//operacoes...
		nota.valor = x;
	}
	public void buildDesconto(){
		double x;
		//operacoes...
		nota.desconto = x;
	}
	public void buildImposto(){
		nota.imposto = nota.valor * 0.07;
	}
	public void buildEmissao(){
		int x;
		//operacoes para obter data (consultar depois)...
		nota.emissao = x;
	}
	public void buildVencimento(){
		nota.vencimento = nota.emissao + 604000;
		// numero de milissegundos equivalentes a 7 dias
	}
	public void buildEmpresa(){
		String x;
		//operacoes...
		nota.empresa = x;
	}
	public void buildValorTotal(){
		nota.valorTotal = nota.valor + nota.imposto - nota.desconto;
	}
}

public class SPBuilder extends notaBuilder {
	public void buildValor(){
		double x;
		//operacoes...
		nota.valor = x;
	}
	public void buildDesconto(){
		double x;
		//operacoes...
		nota.desconto = x;
	}
	public void buildImposto(){
		nota.imposto = nota.valor * 0.06;
	}
	public void buildEmissao(){
		int x;
		//operacoes para obter data...
		nota.emissao = x;
	}
	public void buildVencimento(){
		nota.vencimento = nota.emissao + 345600;
		// numero de milissegundos equivalentes a 4 dias
	}
	public void buildEmpresa(){
		String x;
		//operacoes...
		nota.empresa = x;
	}
	public void buildValorTotal(){
		nota.valorTotal = nota.valor + nota.imposto - nota.desconto;
	}
}

public class EmpresaDirector {
	protected notaBuilder empr;
	public EmpresaDirector(notaBuilder empr){
		this.empr = empr;
	}
	public void buildNota() {
		empr.buildValor();
		empr.buildDesconto();
		empr.buildImposto();
		empr.buildEmissao();
		empr.buildVencimento();
		empr.buildEmpresa();
		empr.buildValorTotal();
	}
	public Nota getNota() {
		return empr.getNota();
	}
}

public class Client {
	public static void main(String[] args) {
		EmpresaDirector empr = new EmpresaDirector(new minasBuilder());
		empr.buildNota();
		Nota nota = empr.getNota();
		System.out.println("Nota de "+nota.empresa+"\nValor: "+nota.valor+"\nDesconto: "+nota.desconto+"\nDedução de Impostos: "+nota.imposto+"\nEmitido em: "+nota.emissao+"\nVencimento em: "+nota.vencimento+"\n\nValor total:"+nota.valorTotal+"\n");
		//para mesma classe nota, outro builder
		empr = new EmpresaDirector (new SPBuilder());
		empr.buildNota();
		nota = empr.getNota();
		System.out.println("Nota de "+nota.empresa+"\nValor: "+nota.valor+"\nDesconto: "+nota.desconto+"\nDedução de Impostos: "+nota.imposto+"\nEmitido em: "+nota.emissao+"\nVencimento em: "+nota.vencimento+"\n\nValor total:"+nota.valorTotal+"\n");
	}
}