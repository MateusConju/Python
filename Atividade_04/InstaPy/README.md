# Desafio: O Pipeline de Processamendo de Mídia

**Cenário**: Você está construindo o backend de uma rede social de fotos (tipo Instagram). Quando um usuário faz umpload de uma imagem em alta resolução, o sistema precisa:

1. Receber o upload imediatamente (**API**).
2. Gerar 3 versões da imagem: Thumbnail, Mobile e Desktop (**Heavy Process**).
3. Aplicar um filtro de "Melhoria Automática" (**Heavy Process**).
4. Atualizar o Feed dos usuários.

## O Problema da engenharia:
Se gerarmos as imagens na hora do upload, o request vai demorar 10 segundos, o usuário vai dessistir. Precisamos aceitar o upload, mostrar o status "Processando..." e, quando acabar, atualizar para "Pronto".

### Cache Validation:
O Feed de imagens (GET /feed) é muito acessado e deve ser cacheado. Porém, quando uma imagem termina de processar no background, o Feed precisa refletir o novo status("Pronto") imediatamaente, sem esperar o TTL do cache expirar. O wworker deve ter poder de limpar o cache da API.