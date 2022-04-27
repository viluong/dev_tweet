
export default {
  getTweets (state, tweets) {
    state.tweets = tweets.data || []
    state.result_count = tweets.meta.result_count
  },
  getMe (state, user) {
    state.user = user.data
  }
}
