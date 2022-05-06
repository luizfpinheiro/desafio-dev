<template>
  <v-app>
    <v-app-bar
      app
      color="grey lighten-3"
    >
      <div class="d-flex align-center">
        <h1> Lista de Transações </h1>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/luizfpinheiro/desafio-dev"
        target="_blank"
        text
      >
        <span class="mr-2">Projeto no Github</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <ListaTransacoes/>
    </v-main>
  </v-app>
</template>

<script>
import ListaTransacoes from './components/ListaTransacoes';

export default {
  name: 'App',

  components: {
    ListaTransacoes,
  },

  data: () => ({
    //
  }),
};
</script>
