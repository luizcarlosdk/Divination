<template>
  <v-container class="fill-height pa-0">
    <v-row>
      <v-col class="chats" cols="4">
        <v-icon
          class="new-chat"
          color="white"
          icon="mdi-plus-circle"
          size="large"
          @click="createChat"
        ></v-icon>
        <div class="chats">
          <v-list v-for="(chat, i) in chats" :key="i" class="chat-preview">
            <v-list-item-content>
              {{ chat }}
            </v-list-item-content>
          </v-list>
        </div>
      </v-col>
      <v-col class="current-chat">
        <v-card>
          <v-card-title>Chat Dungeons and Dragons</v-card-title>
          <v-card-text>
            <v-card class="message-box mb-4">
              <v-list>
                <v-list-item v-for="(message, i) in messages" :key="i">
                  <v-list-item-content class="chat-message">{{
                    message
                  }}</v-list-item-content>
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
    chats: ['Chat 1 aaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'Chat 2', 'Chat 3'],
  }),

  methods: {
    createChat() {
      this.chats.push('New Chat')
    },
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
.new-chat {
  align-self: center;
  margin-bottom: 1em;
}
.chats {
  display: flex;
  flex-direction: column;

  border-radius: 1.5em 0em 0em 1.5em;
  max-height: 760px; /* Set a max height for scrolling */
  overflow-y: auto; /* Enable vertical scrolling */
  padding: 1em; /* Optional padding */
}
.current-chat {
  border-radius: 0em 1.5em 1.5em 0em;
  background-color: rgb(61, 13, 61);
}

.chat-preview {
  background-color: #b2a0d3;
  display: flex;
  justify-self: center;
  align-items: center;
  padding: 1em;
  border-radius: 1em 0.5em 0.5em 1em;
  margin-bottom: 1em;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis ' [..]';
  max-height: 50px;
}
.message-box {
  background-color: white;
  min-height: 600px;
  max-height: 300px;
  overflow-y: auto;
  padding: 0px;
}

.chat-message {
  font-size: 140%;
  font-family: verdana;
}
</style>
