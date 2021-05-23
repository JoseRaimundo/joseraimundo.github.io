class No:
    # Estrutura que representa o nó da árvore,
    # O nó guarda o valor, e uma referência para seus nós filhos (direita e esquerda)

    def __init__(self, valor, dir, esq):
        self.item = valor
        self.dir = dir
        self.esq = esq

class Arvore:

    # Método para criar uma árvore vazia, basicamente cria o local para o primeiro nó (raiz)
    def __init__(self):
        self.raiz = No(None,None,None)
        self.raiz = None

    # Método para inserir um valor (novo nó)
    def inserir(self, v):
        # Cria um nó novo com um valor e galhos vazios
        novoNo = No(v,None,None)
        ############# Determina a posição do nó na árvore #########
        # Se a raiz estiver vazia, então o nó será a raiz
        if self.raiz == None:
            self.raiz = novoNo
        else:
        # se a raiz não estiver vazia, pega o nó raiz como nó atual, 
        # esse nó será usado iniclamente como ponto de referência 
        # para localizar o lugar correto do novo nó
            atualNo = self.raiz
            while True:
                anteriorNo = atualNo
                # se o valor do nó novo for menor ou igual que o valor 
                # do nó atual, então insere o valor na esquerda
                if v <= atualNo.item:
                    atualNo = atualNo.esq
                    # Verifica se é o nó final do galho
                    if atualNo == None:
                        anteriorNo.esq = novoNo
                        return
                # Caso contrário, insere o valor para a direita
                else:
                    atualNo = atualNo.dir
                    # Verifica se é o nó final do galho
                    if atualNo == None:
                            anteriorNo.dir = novoNo
                            return
                ## Se a verificação não chegar no nó final do galho, 
                # então retorna para o começo do while


    def buscar(self, chave):
        # Lembrar de verificar sempre se a árvore tá vazia
        if self.raiz == None:
            return None
        # Pega no nó raiz para usar como referência para iniciar a procura
        atual = self.raiz
         # enquanto nao encontrou
        while atual.item != chave:
            # Se o valor for menor que o nó atual, então vai deslocar a pesquisa
            # para a esquerda, se não vai para a direita
            if chave < atual.item:
                atual = atual.esq
            else:
                atual = atual.dir
            # Se encontrou um galho vazio (filha) e não bateu com valor,
            # então termina a busca sem achar nada
            if atual == None:
                return None
            # Se encontar algo retornará após o termino do while
            return atual

    # Apaga usando o nó sucessor, que é o nó mais a esquerda
    # da subarvore a direita do nó informado
    def nosucessor(self, apaga):
        paidosucessor = apaga
        sucessor = apaga
        # Usa a subarvore a direita como referência para identificar quem vai ser apagado
        atual = apaga.dir

        # Percorre a subarvore enquanto não chegar no nó mais a esquerda
        while atual != None: 
            paidosucessor = sucessor
            sucessor = atual
            # Chagando na posição usada como referência, caminha para a esquerda
            atual = atual.esq
        # se sucessor nao é o filho a direita do nó que deverá ser eliminado
        # então será o nó que herda os galhos do sucessor que estão a direita
        if sucessor != apaga.dir:
            paidosucessor.esq = sucessor.dir
            sucessor.dir = apaga.dir
        return sucessor

    # Método para remover um nó
    def remover(self, v):
        # Lembrar de sempre verificar se arvore vazia
        if self.raiz == None:
            return False
        # Pegar a raiz como referência inicial
        atual = self.raiz
        # Salvar uma referância anterior para realozar as subarvores filhas do nó apagado
        pai = self.raiz
        filho_esq = True
        # Realiza uma busca normal, só atualizando a referência do nó anterior
        while atual.item != v:
            pai = atual
            if v < atual.item:
                atual = atual.esq
                filho_esq = True 
            else:
                atual = atual.dir 
                filho_esq = False
            if atual == None:
                return False

        # Se nao possui nenhum filho então só apaga
        if atual.esq == None and atual.dir == None:
            if atual == self.raiz:
                self.raiz = None # se raiz
            else:
                if filho_esq:
                        pai.esq =  None # se for filho a esquerda do pai
                else:
                        pai.dir = None # se for filho a direita do pai

        # Tratamento se é pai e nao possui um filho a direita
        elif atual.dir == None:
            if atual == self.raiz:
                self.raiz = atual.esq
            else:
                if filho_esq:
                        pai.esq = atual.esq
                else:
                        pai.dir = atual.esq

        # Tratamento se é pai e nao possui um filho a esquerda
        elif atual.esq == None:
            if atual == self.raiz:
                self.raiz = atual.dir
            else:
                if filho_esq:
                        pai.esq = atual.dir
                else:
                        pai.dir = atual.dir

        # Tratamento quando as subarvores completa
        else:
            sucessor = self.nosucessor(atual)
            if atual == self.raiz:
                self.raiz = sucessor
            else:
                if filho_esq:
                        pai.esq = sucessor
                else:
                        pai.dir = sucessor 
            sucessor.esq = atual.esq

        return True

    # Printa a organização in ordem
    def inOrder(self, atual):
        if atual != None:
            self.inOrder(atual.esq)
            print(atual.item,end=" ")
            self.inOrder(atual.dir)
    # Printa em organização pré-ordem
    def preOrder(self, atual):
        if atual != None:
            print(atual.item,end=" ")
            self.preOrder(atual.esq)
            self.preOrder(atual.dir)
    # Printa em organização pós-ordem
    def posOrder(self, atual):
        if atual != None:
            self.posOrder(atual.esq)
            self.posOrder(atual.dir)
            print(atual.item,end=" ")

    # Retorna a altura da árvore
    def altura(self, atual):
        if atual == None or atual.esq == None and atual.dir == None:
            return 0
        else:
            if self.altura(atual.esq) > self.altura(atual.dir):
                return  1 + self.altura(atual.esq)
            else:
                return  1 + self.altura(atual.dir)
    # Retorna a quantidade de folhas
    def folhas(self, atual):
        if atual == None:
            return 0
        if atual.esq == None and atual.dir == None:
            return 1
        return self.folhas(atual.esq) + self.folhas(atual.dir)
    # Retorna a quantidade de nós
    def contarNos(self, atual):
        if atual == None:
                return 0
        else:
                return  1 + self.contarNos(atual.esq) + self.contarNos(atual.dir)
    # Retorna o valor mínimo
    def minn(self):
        atual = self.raiz
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.esq
        return anterior
    # Retorna o valor máximo
    def maxx(self):
        atual = self.raiz
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.dir
        return anterior

    def caminhar(self):
        print(" Exibindo em ordem: ",end="")
        self.inOrder(self.raiz)
        print("\n Exibindo em pos-ordem: ",end="")
        self.posOrder(self.raiz)
        print("\n Exibindo em pre-ordem: ",end="")
        self.preOrder(self.raiz)
        print("\n Altura da arvore: %d" %(self.altura(self.raiz)))
        print(" Quantidade de folhas: %d"  %(self.folhas(self.raiz)))
        print(" Quantidade de Nós: %d" %(self.contarNos(self.raiz)))
        if self.raiz != None: # se arvore nao esta vazia
            print(" Valor minimo: %d" %(self.minn().item))
            print(" Valor maximo: %d" %(self.maxx().item))

## Colocar o código acima em um arquivo chamdo arvores.py
## Colocar o código abaixo em um arquivo chamado main.py
## Descomentar o código abaixo
# import arvore as Arvore
arv = Arvore()
opcao = 0
while opcao != 5:
     print("***********************************")
     print("Entre com a opcao:")
     print(" --- 1: Inserir")
     print(" --- 2: Excluir")
     print(" --- 3: Pesquisar")
     print(" --- 4: Exibir")
     print(" --- 5: Sair do programa")
     print("***********************************")
     opcao = int(input("-> "))
     if opcao == 1:
          x = int(input(" Informe o valor -> "))
          arv.inserir(x)
     elif opcao == 2:
          x = int(input(" Informe o valor -> "))
          if arv.remover(x) == False:
               print(" Valor nao encontrado!")
     elif opcao == 3:
          x = int(input(" Informe o valor -> "))
          if arv.buscar(x) != None:
               print(" Valor Encontrado")
          else:
               print(" Valor nao encontrado!")	 
     elif opcao == 4:
          arv.caminhar()
     elif opcao == 5:
          break