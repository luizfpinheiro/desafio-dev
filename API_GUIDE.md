### ROTAS DA API
#### http://127.0.0.1:8000/importar-remessa (Rota de upload do arquivo CNAB)
    - Somente método POST.
    - Somente arquivos .txt são aceitos (baseado no arquivo informado).
    - Corpo da requisição deve ser do tipo "multipart/form-data" e o arquivo deve ser chamar 'file'.
    - Retorna as informaçẽos do arquivo parseadas.

#### http://localhost:8000/transacoes (Listagem de transacoes existentes, com base nos dados importados via upload do arquivo CNAB)
        - Somente método GET.
        - Retorna lista com transacoes existentes, organizada por nome da loja.