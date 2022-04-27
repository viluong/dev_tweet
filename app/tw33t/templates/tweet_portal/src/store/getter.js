export default {
	getTweets: (state) => {
		return state.tweets
	},
	getMe: (state) => {
		return state.user
	},
	getCount: (state) => {
		return state.result_count
	}
}
