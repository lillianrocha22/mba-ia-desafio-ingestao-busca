from search import search_prompt, relevant_docs

def main():
    chain = search_prompt()

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    
    print("Digite sua pergunta ou 'sair' para encerrar.")

    while True:
        pergunta_usuario = input("\nPERGUNTA: ")
        if pergunta_usuario.lower() == 'sair':
            print("Encerrando o chat. Até logo!")
            break

        relevant_docs = get_relevant_documents(pergunta_usuario, k=10)

        contexto = "\n\n".join([doc.page_content for doc in relevant_docs])

        resposta = chain.invoke({"contexto": contexto, "pergunta": pergunta_usuario})

        print(f"RESPOSTA: {resposta}")

if __name__ == "__main__":
    main()