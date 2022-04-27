import axios from 'axios'

const baseURI = 'http://localhost:8000/'

export default {
  getTweets({commit}, search=null) {
    let path = 'get_tweets'
    if (search){
      path = path + '?search=' + search
    }
    axios.get(baseURI + path).then((response) => {
      const tweets = response.data
      commit('getTweets', tweets)
    })
  },
  getMe({commit}) {
    let path = 'me'    
    axios.get(baseURI + path).then((response) => {
      const user = response.data
      commit('getMe', user)
    })
  }
}
