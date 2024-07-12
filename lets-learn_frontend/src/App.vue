<template>
  <nav class="bg-gradient-to-r from-violet-200 to-pink-200">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="relative flex h-16 items-center justify-between">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
          <!-- Mobile menu button-->
          <button type="button" @click="isOpenMobile = !isOpenMobile"
            class="relative inline-flex items-center justify-center rounded-md p-1 text-violet-800 hover:bg-violet-100 hover:text-violet-800 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-violet-800"
            aria-controls="mobile-menu" aria-expanded="false">
            <span class="absolute -inset-0.5"></span>
            <span class="sr-only">Open main menu</span>
            <!--
            Icon when menu is closed.

            Menu open: "hidden", Menu closed: "block"
          -->
            <svg class="block h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
              aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
            </svg>
            <!--
            Icon when menu is open.

            Menu open: "block", Menu closed: "hidden"
          -->
            <svg class="hidden h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
              aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <div class="flex items-center justify-center sm:items-stretch sm:justify-start">
          <div class="flex text-white flex-shrink-0 items-center ml-10 md:ml-0 font-bold">
            <router-link to="/" class="flex text-violet-800">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="size-6 mr-1">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25" />
              </svg>

              Lets Learn</router-link>

          </div>
          <div class="hidden sm:ml-6 sm:block">
            <div class="ml-6 space-x-6">
              <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
              <router-link to="/dashboard" v-if="$store.state.isAuthenticated"
                class="text-violet-800 text-sm hover:bg-violet-100 px-2 py-1 rounded duration-300">Dashboard</router-link>
              <router-link to="/courses"
                class="text-violet-800 text-sm hover:bg-violet-100 px-2 py-1 rounded duration-300">Courses</router-link>
              <router-link to="/categories"
                class="text-violet-800 text-sm hover:bg-violet-100 px-2 py-1 rounded duration-300">Categories</router-link>
              <router-link to="/about"
                class="text-violet-800 text-sm hover:bg-violet-100 px-2 py-1 rounded duration-300">About</router-link>


            </div>
          </div>
        </div>
        <div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">


          <!-- Profile dropdown -->
          <div class="relative ml-3 flex invisible md:visible">
            <template v-if="!$store.state.isAuthenticated">
              <router-link class="relative flex text-violet-800 text-sm hover:bg-pink-100 text-sm px-2 py-1 rounded"
                to="/sign-in">Sign
                in</router-link>
            </template>

            <template v-if="$store.state.isAuthenticated">
              <div>
                <button @click="isOpen = !isOpen"
                  class="relative flex text-violet-800 bg-pink-100 text-sm px-2 py-1 rounded" id="user-menu-button"
                  aria-expanded="false" aria-haspopup="true">
                  <span class="absolute -inset-1.5"></span>
                  <span class="sr-only">Open user menu</span>
                  {{ currentUser ? currentUser.first_name + ' ' + currentUser.last_name : 'Loading...' }}
                  <span v-if="!isOpen">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                      stroke="currentColor" class="size-4 ml-1">
                      <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
                    </svg>
                  </span>
                  <span v-else>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                      stroke="currentColor" class="size-4 ml-1">
                      <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 15.75 7.5-7.5 7.5 7.5" />
                    </svg>

                  </span>


                </button>
              </div>


              <div v-if="isOpen"
                class="absolute right-0 z-10 mt-8 w-48 duration-300 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
                role="menu" aria-orientation="vertical" aria-labelledby="user-menu-button" tabindex="-1">
                <!-- Active: "bg-gray-100", Not Active: "" -->
                <ul>
                  <li class="hover:bg-indigo-100"><router-link @click="isOpen = false" to="/profile"
                      class="block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1"
                      id="user-menu-item-0">Account</router-link></li>
                  <li class="hover:bg-indigo-100"> <button @click="logout()"
                      class="block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1"
                      id="user-menu-item-2">Sign out</button></li>
                </ul>



              </div>
            </template>

          </div>
        </div>
      </div>
    </div>

    <!-- Mobile menu, show/hide based on menu state. -->
    <div v-if="isOpenMobile" class="sm:hidden" id="mobile-menu">
      <div class="space-y-1 px-2 pb-3 pt-2">
        <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
        <div>
          <router-link to="/sign-in" v-if="!$store.state.isAuthenticated" class="text-violet-800 text-sm font-medium"
            aria-current="page">Sign in</router-link>
        </div>
        <div>
          <router-link to="/" class="text-violet-800 text-sm font-medium" aria-current="page">Courses</router-link>
        </div>
        <div>
          <router-link to="/dashboard" v-if="$store.state.isAuthenticated"
            class="text-violet-800 text-sm font-medium">Dashboard</router-link>
        </div>

      </div>
    </div>
  </nav>
  <router-view />
</template>
<script>
import axios from 'axios'

export default {
  data() {
    return {
      isOpen: false,
      isOpenMobile: false,
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common["Authorization"] = `Token ${token}`
    }
    else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  methods: {
    logout() {

      this.isOpen = false
      axios.defaults.headers.common["Authorization"] = ""

      localStorage.removeItem("token")
      localStorage.removeItem("username")
      localStorage.removeItem("userid")

      this.$store.commit('removeToken')
      this.$router.push('/sign-in')

    }
  },

}
</script> -->