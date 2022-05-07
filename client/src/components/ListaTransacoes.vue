<template>
  <div>
    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on, attrs }">
        <v-btn class="ma-2" color="success" v-bind="attrs" v-on="on">
          IMPORTAR DADOS
          <v-icon right dark> mdi-cloud-upload </v-icon>
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Selecionar Arquivo
        </v-card-title>

        <v-card-text>
          <v-file-input
            v-model="arquivo_importacao"
            class="ma-5"
            accept=".txt"
            label="Inserir arquivo"
            outlined
            dense
          ></v-file-input>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="success" @click="importarArquivo"> Enviar </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-expansion-panels v-model="panel" multiple dense class="ma-3">
      <v-expansion-panel v-for="(item, i) in transacoes" :key="i">
        <v-expansion-panel-header class="grey lighten-3 font-weight-medium">
          {{ item.nome_loja }}
          <v-spacer></v-spacer>
          <span class="ma-2 text--uppercase">Saldo: R$ {{ item.saldo }}</span>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-data-table
            dense
            :headers="headers"
            :items="item.transacoes"
            :items-per-page="10"
            class="elevation-1"
          ></v-data-table>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
import api from "@/utils";

export default {
  name: "ListaTransacoes",

  data: () => ({
    transacoes_url: "/transacoes",
    importacao_url: "/importar-remessa",
    transacoes: [],
    panel: [0, 1, 2, 3, 4, 5],
    headers: [
      { text: "ID", value: "id" },
      { text: "Tipo", value: "tipo__descricao" },
      { text: "Valor", value: "valor" },
      { text: "Cartão", value: "cartao" },
      { text: "Representante", value: "nome_representante" },
    ],
    dialog: false,
    arquivo_importacao: null,
  }),
  mounted() {
    this.getTransacoes();
  },
  methods: {
    getTransacoes() {
      api
        .get(this.transacoes_url)
        .then((response) => {
          response.data.forEach((element) => {
            this.transacoes.push(element);
          });
        })
        .catch((err) => {
          console.error(err);
        });
    },
    importarArquivo() {
      let formData = new FormData();
      formData.append("file", this.arquivo_importacao);

      api
        .post(this.importacao_url, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          if (response.status == 200) {
            this.dialog = false;
            window.location.reload();
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>
