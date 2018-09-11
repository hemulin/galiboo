import Vue from 'vue';

export default function({ $axios, redirect, app, store }) {
  $axios.onRequest((config) => {
    if (!(process.env.NODE_ENV === 'production')) {
      // Vue.$log.debug('Making request to', config.url)
      console.log('Making request to', config.url);
    }
  });

  $axios.onError((error) => {
    // const code = parseInt(error.response && error.response.status)
    if (error.request.responseURL.endsWith('investment-request') && error.response.status === 404) {
      // Vue.$log.debug("user's investment request couldn't be found")
      console.log("user's investment request couldn't be found");
      return;
    }
    if (error.request.responseURL.endsWith('investment-request') && error.response.status === 403) {
      // Vue.$log.debug("user's investment request already exist")
      console.log("user's investment request already exist");
      return;
    }
    Vue.$log.error('axios call error', error.response.status);
    if (error.code === 'ECONNREFUSED') {
      // Vue.$log.error('Error: Backend not responding')
      console.log('Error: Backend not responding');
    }
    // if (code === 400) {
    //   redirect('/400')
    // }
    // store.dispatch('error', error)
  });
}
