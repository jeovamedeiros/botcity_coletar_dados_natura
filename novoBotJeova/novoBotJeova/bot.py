
import mysql.connector


from botcity.web import WebBot, Browser

class Bot(WebBot):
    def action(self, execution=None):

        self.headless = False

        # Uncomment to set the WebDriver path
        self.driver_path = "./chromedriver.exe"

        self.browse("https://www.natura.com.br")

        if not self.find( "lupa", matching=0.97, waiting_time=10000):
            self.not_found("lupa")
        self.click()

        self.paste("essencial")
        self.enter()

        if not self.find( "essencial", matching=0.97, waiting_time=10000):
            self.not_found("essencial")
        self.click_relative(194, 273)

        if not self.find( "nomeEssencial", matching=0.97, waiting_time=10000):
            self.not_found("nomeEssencial")
        self.triple_click_relative(768, 151)

        self.control_c()
        self.control_v()

        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()

        produto1 = self.get_clipboard()

        if not self.find( "valorAntigo", matching=0.97, waiting_time=10000):
            self.not_found("valorAntigo")
        self.click_relative(-469, 513)

        self.control_c()
        self.control_v()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()

        promocaoProduto1 = self.get_clipboard()

        if not self.find( "valorNovoEssencial", matching=0.97, waiting_time=10000):
            self.not_found("valorNovoEssencial")
        self.double_click_relative(87, 160)

        self.control_c()
        self.control_v()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()

        valorProduto1 = self.get_clipboard()



        if not self.find( "pagamento ", matching=0.97, waiting_time=10000):
             self.not_found("pagamento ")
        self.triple_click_relative(4, 45)

        self.control_c()
        self.control_v()
        pagamento = self.get_clipboard()

        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()

        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        print("NOME ESSENCIAL: " + produto1)
        print("O valor do produto era: R$ " + promocaoProduto1 + " e agora está por R$" + valorProduto1)
        print("A FORMA DE PAGAMENTO É: " + pagamento)

        if not self.find( "lupa2", matching=0.97, waiting_time=10000):
          self.not_found("lupa2")
        self.click_relative(77, 17)

        self.paste("sintonia")
        self.enter()
        
        
        if not self.find( "encontrarSintoniaa", matching=0.97, waiting_time=10000):
            self.not_found("encontrarSintoniaa")
        self.click_relative(635, 256)
    
        if not self.find( "nomsintonia", matching=0.97, waiting_time=10000):
            self.not_found("nomsintonia")
        self.triple_click_relative(831, 148)

        self.control_c()
        self.control_v()

        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()

        produtoSintonia = self.get_clipboard()

        if not self.find( "valorSintonia", matching=0.97, waiting_time=10000):
           self.not_found("valorSintonia")

        self.double_click_relative(-28, 122)

        self.control_c()
        self.control_v()

        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()

        valorSintonia = self.get_clipboard()

        if not self.find( "pagamentoSintonia", matching=0.97, waiting_time=10000):
          self.not_found("pagamentoSintonia")
        self.triple_click_relative(217, 46)

        self.control_c()
        self.control_v()

        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()

        self.wait(10000)

        pagamentoSintonia = self.get_clipboard()
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")

        print("NOME SINTONIA: " + produtoSintonia)
        print("VALOR PRODUTO SINTONIA: R$ " + valorSintonia)
        print("A FORMA DE PAGAMENTO É: " + pagamentoSintonia)

        if not self.find( "lupa3", matching=0.97, waiting_time=10000):
         self.not_found("lupa3")
        self.click_relative(72, 17)

        self.paste("kaiak")
        self.enter()

        self.page_down()
        
        if not self.find( "procurarKaikkkk", matching=0.97, waiting_time=10000):
            self.not_found("procurarKaikkkk")
        self.click_relative(-89, 498)
        

        if not self.find( "nomeKaiak", matching=0.97, waiting_time=10000):
            self.not_found("nomeKaiak")
        self.triple_click_relative(582, 156)

        self.control_c()
        self.control_v()

        nomeKaik = self.get_clipboard()

        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()

        if not self.find( "valorKaiak", matching=0.97, waiting_time=10000):
          self.not_found("valorKaiak")
        self.double_click_relative(26, 125)

        self.control_c()
        self.control_v()

        valorAntigoKaiak = self.get_clipboard()

        if not self.find( "valorAtual", matching=0.97, waiting_time=10000):
            self.not_found("valorAtual")
        self.double_click_relative(76, 88)

        self.control_c()
        self.control_v()

        valorKaiak = self.get_clipboard()

        if not self.find( "formaPagamentoKaiak", matching=0.97, waiting_time=10000):
           self.not_found("formaPagamentoKaiak")
        self.triple_click_relative(86, 45)

        self.control_c()
        self.control_v()

        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()

        pagamentoKaiak = self.get_clipboard()

        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        print("NOME KAIAK: " + nomeKaik)
        print("O valor do produto era: R$ " + valorAntigoKaiak + " e agora está por R$" + valorKaiak)
        print("A FORMA DE PAGAMENTO É: " + pagamentoKaiak)

        if not self.find( "lupa3", matching=0.97, waiting_time=10000):
           self.not_found("lupa3")

        self.click_relative(99, 20)

        self.paste("biografia")
        self.enter()
        
        
        if not self.find( "procurarBiografia", matching=0.97, waiting_time=10000):
            self.not_found("procurarBiografia")
        self.click_relative(619, 258)
        
        if not self.find( "nomeBiografia", matching=0.97, waiting_time=10000):
            self.not_found("nomeBiografia")
        self.triple_click_relative(796, 157)

        self.control_c()
        self.control_v()

        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()

        nomeB = self.get_clipboard()

        if not self.find( "verValorAtualBio", matching=0.97, waiting_time=10000):
          self.not_found("verValorAtualBio")
        self.double_click_relative(90, 84)

        self.control_c()
        self.control_v()

        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()

        valorAntigoBiografia = self.get_clipboard()

        if not self.find( "verValorAtual", matching=0.97, waiting_time=10000):
           self.not_found("verValorAtual")
        self.double_click_relative(91, 40)

        self.control_c()
        self.control_v()

        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()

        valorAtualBiografia = self.get_clipboard()

        if not self.find( "pagamentoBio", matching=0.97, waiting_time=10000):
          self.not_found("pagamentoBio")
        self.triple_click_relative(130, 118)

        self.control_c()
        self.control_v()

        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()

        pagamentoBiografia = self.get_clipboard()

        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()
        self.page_up()

        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        print("NOME BIOGRAFIA: " + nomeB)
        print("O valor do produto era: R$ " + valorAntigoBiografia + " e agora está por R$" + valorAtualBiografia)
        print("A FORMA DE PAGAMENTO É: " + pagamentoBiografia)
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")

        # Wait for 10 seconds before closing
        # self.wait(10000)

        # Stop the browser and clean up
        #self.stop_browser()

        conexao = mysql.connector.connect(

            host='localhost',
            user='root',
            password='root',
            database='NATURAJEOVA',

        )
        print("Conexão bem sucedida")

        cursor = conexao.cursor()

        id = 4
        produto = input("Digite o nome do produto")
        preco = input("Digite o preço do produto desejado")
        quantidade = 1

        comando = f"INSERT INTO PRODUTOS (ID, CLIENTE, PRODUTO, PRECO, QUANTIDADE) VALUES ( {id},'{cliente}','{produto}',{preco},{quantidade})"

        cursor.execute(comando)
        conexao.commit()


    def not_found(self, label):
        print(f"Element not found: {label}")


cliente = input("Digite o seu Nome: ")
print("Abrindo o navegador:::")


















if __name__ == '__main__':
    Bot.main()



















