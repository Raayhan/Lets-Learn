import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignIn from '@/views/auth/SignIn.vue'
import AboutView from '@/views/AboutView.vue'
import SignUp from '@/views/auth/SignUp.vue'
import Dashboard from '@/views/Dashboard.vue'
import Courses from '@/views/Courses.vue'
import Categories from '@/views/Categories.vue'

import store from '../store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
   {
    path: '/sign-in',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/courses',
    name: 'Courses',
    component: Courses
  },
  {
    path: '/categories',
    name: 'Categories',
    component: Categories
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      requireLogin:true
    }

  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'SignIn', query: { to: to.path } });
  }
  if ((to.name === 'SignIn' || to.name === 'SignUp') && store.state.isAuthenticated) {
    next({ name: 'Dashboard' })
  } 
  else {
    next()
  }
})
export default router