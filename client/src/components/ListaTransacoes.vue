<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="items"
      :items-per-page="10"
      class="elevation-1"
    ></v-data-table>
  </div>
</template>

<script>
import api from "@/utils";

export default {
  name: "ListaTransacoes",

  data: () => ({
    transacoes_url: "/transacoes",
    items: [],
    headers: [
      { text: "ID", value: "id"},
      { text: "Tipo", value: "tipo"},
      { text: "Valor", value: "cpf"},
      { text: "Cartão", value: "cartao"},
      { text: "Representante", value: "nome_representante"},
      { text: "Loja", value: "nome_loja"},
    ]
  }),
  mounted() {
    this.getTransacoes();
  },
  methods: {
    getTransacoes() {
      api
        .get(this.transacoes_url)
        .then((response) => {
          response.data.forEach(element => {
            this.items.push(element);
          });
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>
