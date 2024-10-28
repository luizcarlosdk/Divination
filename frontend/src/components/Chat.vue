<template>
  <v-container class="fill-height pa-0">
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>Chat Dungeons and Dragons</v-card-title>
          <v-card-text class="flex-shrink-1">
            <v-text-field
              v-model="inputText"
              label="Digite sua pergunta"
              type="text"
              no-details
              outlined
              append-outer-icon="send"
              hide-details
            />
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    inputText: '',
  }),
}
</script>

<style>
</style>