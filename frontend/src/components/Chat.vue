<template>
  <v-container fluid class="pa-2">
    <v-row>
      <v-col class="chats-column" cols="4">
        <div class="add-new-chat">
          <v-btn
            @click="createChat"
            color="rgb(61, 13, 61)"
            class="new-chat-button"
          >
            Criar novo chat
            <v-icon
              color="white"
              icon="mdi-plus-circle"
              size="large"
              end
            ></v-icon>
          </v-btn>
        </div>
        <div class="chats">
          <v-list class="chats-list">
            <v-list-item
              v-for="(chat, i) in chats"
              :key="i"
              class="chat-preview"
              rounded="x1"
              color="#033"
              @click="selectChat(i, chat.chat_id)"
            >
              <v-list-item-content>
                {{ this.chats[i].messages[1] ? this.chats[i].messages[1] : `Chat ${i + 1}` }}
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </div>
      </v-col>
      <v-col class="current-chat" cols="8">
        <v-card class="chat-card">
          <v-card-title>{{this.current_messages[0]}}</v-card-title>
          <v-card-text>
            <v-card class="message-box mb-4">
              <v-list>
                <v-list-item v-for="(message, i) in current_messages" :key="i">
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
              @click:append-inner="sendMessage(current_chat_id)"
              @keyup.enter="sendMessage(current_chat_id)"
            />
          </v-card-text>
        </v-card>
      </v-col>
      <v-btn @click="changePersonality('creative')" >Personalidade Criativa</v-btn>
      <v-btn @click="changePersonality('default')" >Personalidade Restritiva</v-btn>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data: () => ({
    current_chat_id: null,
    current_messages: [],
    inputText: '',
    loading: false,
    chats: [],
  }),

  async beforeMount() {
    const base_url = import.meta.env.VITE_BACKEND_URL
  
    
    try {
      const response = await axios.get(`${base_url}/v1/chats`)
      const data = response.data.projectHistory 
      console.log(data)
      var chats = Object.keys(data).map(
        chatId => ({
          chat_id: chatId,
          messages: data[chatId].messages.map(msg => msg.content) || []
        })
      )
      this.chats = chats
    }
    catch {
      console.log("retrieve chats had a problem")
    }

  },
  mounted() {
    this.createChat()
  },
  methods: {
    selectChat(index, id) {
      console.log('chat_index:' + index + 'chat_id: ' + id)
      this.current_chat_id = id

      const selectedChat = this.chats.find(chat => chat.chat_id === id);

      this.current_messages = selectedChat ? selectedChat.messages : [];

    },
    async createChat() {
      const base_url = import.meta.env.VITE_BACKEND_URL

      try {
        const response = await axios.post(`${base_url}/v1/chats`, {})
        this.chats.push({
          "chat_id": response.data.chatId,
          messages: []
        })
        this.current_chat_id = response.data.chatId
        const selectedChat = this.chats.find(chat => chat.chat_id === this.current_chat_id)
        this.current_messages = selectedChat.messages
      } catch {
        console.log()
      }


    },
    async sendMessage(actual_chat_id) {
      const base_url = import.meta.env.VITE_BACKEND_URL

      if(actual_chat_id == null) {
        alert("Nenhum chat for selecionado")
        return
      }

      if (this.inputText.trim() === '') return
      const actualChat = this.chats.find(chat => chat.chat_id === actual_chat_id);
      actualChat.messages.push(this.inputText)
      const question = this.inputText
      this.inputText = ''
      try {
        const response = await axios.post(`${base_url}/v1/answer`, {
          user_question: question,
          chat_id: actual_chat_id,
        })
        console.log(response)
        const actualChat = this.chats.find(chat => chat.chat_id === actual_chat_id);
        actualChat.messages.push(response.data.projectAnswer)
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
.chats-list {
  background-color: rgb(0, 0, 0, 0.3);
}

.chat-card {
  height: 100vh;
}

.chats-column {
  background-color: rgb(0, 0, 0, 0.3);
}

.new-chat {
  align-self: center;
  margin-bottom: 1em;
}

.chats {
  display: flex;
  flex-direction: column;

  border-radius: 1.5em 0em 0em 1.5em;
  max-height: 900px; /* Set a max height for scrolling */
  overflow-y: auto; /* Enable vertical scrolling */
  padding: 1.5em 0.5em; /* Optional padding */
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
  min-height: 60px;
}
.message-box {
  background-color: white;
  min-height: 85vh;
  max-height: 300px;
  overflow-y: auto;
  padding: 0px;
}

.chat-message {
  font-size: 140%;
  font-family: verdana;
}

.add-new-chat {
  display: flex;
  justify-content: center;
}
</style>
