<template>
  <v-container class="fill-height pa-0">
    <v-row>
      <v-col>
        <v-card class="chat">
          <v-card-title>Chat Dungeons and Dragons</v-card-title>
          <v-card-text>
            <v-card class="message-box mb-4">
              <v-list>
                <v-list-item v-for="(message, index) in messages" :key="index">
                  <v-list-item-content>{{ message }}</v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>

            <v-text-field
              :loading="loading"
              variant="solo"
              append-inner-icon="mdi-send"
              v-model="inputText"
              class="text-input"
              label="Digite sua pergunta"
              type="text"
              rounded
              no-details
              append-outer-icon="send"
              hide-details
              @click:append-inner="sendMessage"
              @keyup.enter="sendMessage"
            />
          </v-card-text>
          <div class="personalities">
            <v-btn @click="changePersonality('default')"
              >Personalidade restrita</v-btn
            >
            <v-btn @click="changePersonality('creative')"
              >Personalidade criativa</v-btn
            >
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data: () => ({
    inputText: '',
    loading: false,
    messages: [],
  }),

  methods: {
    async sendMessage() {
      const base_url = import.meta.env.VITE_BACKEND_URL

      if (this.inputText.trim() === '') return
      this.messages.push('Usuário: ' + this.inputText)
      const question = this.inputText
      this.inputText = ''
      try {
        const response = await axios.post(`${base_url}/v1/answer`, {
          user_question: question,
        })
        console.log(response)
        this.messages.push('Bot: ' + response.data.projectAnswer)
      } catch (error) {
        console.error(
          'Error:',
          error.response ? error.response.data : error.message
        )
      }

      // antes de apagar o input enviar para o back
      this.loading = true

      setTimeout(() => {
        this.loading = false
      }, 2000)
    },
    async changePersonality(personality) {
      const base_url = import.meta.env.VITE_BACKEND_URL
      try {
        const response = await axios.post(`${base_url}/v1/context`, {
          new_template: personality,
        })
        this.messages.push(
          'Bot: alterei minha personalidade alterada para: ' + response.data
        )
        console.log(response.data)
      } catch (error) {
        console.error(
          'Error:',
          error.response ? error.response.data : error.message
        )
      }
    },
  },
}
</script>

<style>
.chat {
  background-color: grey;
}
.message-box {
  background-color: white;
  min-height: 600px; /* Set a minimum height */
  max-height: 300px; /* Limit maximum height */
  overflow-y: auto;
  padding: 3px;
}

.personalities {
  display: flex;
  justify-content: space-around;
}
</style>
