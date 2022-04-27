<template>
    <div class="hello">
      <div>
        <p>User: {{user.name}}</p>
      </div>
      <div class="box p-4" >
        <div class="col-6 offset-3">
          <div class="form-group ml-5 mr-5 row">
              <div class="col-10">
                  <input class="form-control" autofocus
                      v-model="search"
                      @keyup.enter="getTweets(search)"
                      placeholder="Input your tweet">
              </div>
              <div class="col-2">
                  <button @click="getTweets(search)" class="btn btn-primary">
                      Search
                  </button>
              </div>
          </div>
        </div>
      </div>
      <br>
      <b-container class="bv-list-tweet">
        <b-row>
          <b-col></b-col>
          <b-col>
            <b-list-group>
              <b-list-group-item class="flex-column align-items-start" v-for="item in tweets" :key="item.id" >
                <div class="d-flex w-100 justify-content-between">
                  <small class="text-muted">{{ item.created_at | datetimeFormat }}</small>
                </div>
                <p class="mb-1">
                  {{ item.text }}
                </p>
              </b-list-group-item>
            </b-list-group>
            <p v-if="result_count == 0">
              Tweets not found
            </p>
          </b-col>
          <b-col></b-col>
        </b-row>
      </b-container>
    </div>
</template>

<script>
import moment from 'moment';
export default {

  name: 'TweetList',

  data: () => {
    return {
      search: null,
      tweets: this.$store.state.tweets.slice(0, 3),
      user: this.$store.state.user,
      result_count: this.$store.state.result_count,
    }
  },
  computed: {
    tweets: function() {
      let tweets = this.$store.state.tweets.slice(0, 3);
      return tweets
    },
    user: function() {
      let user = this.$store.state.user
      return user;
    },
    result_count: function() {
      let result_count = this.$store.state.result_count
      return result_count;
    }
  },
  filters: {
    datetimeFormat: function(value) {
      if (!value) return ''
      return moment(String(value)).format('DD/MM/YYYY hh:mm')
    }
  },
  methods: {
    getTweets (search=null) {
      this.$store.dispatch('getTweets', search)
    },
    getMe () {
      this.$store.dispatch('getMe')
    }
  },
  mounted: function() {
    this.getMe()
    this.getTweets()
  }  
}
</script>
