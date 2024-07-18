import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignIn from '@/views/auth/SignIn.vue'
import AboutView from '@/views/AboutView.vue'
import SignUp from '@/views/auth/SignUp.vue'
import Dashboard from '@/views/Dashboard.vue'
import Courses from '@/views/Courses.vue'
import Categories from '@/views/Categories.vue'
import CourseDetails from '@/views/course/Details.vue'
import Enroll from '@/views/course/Enroll.vue'

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
    path: '/courses/:category_slug/:course_slug',
    name: 'CourseDetails',
    component: CourseDetails
    
  },
    {
    path: '/courses/:category_slug/:course_slug/enroll',
    name: 'EnrollCourse',
    component: Enroll,
    meta: {
      requireLogin:true
    }
    
  },
  {
    path: '/categories',
    name: 'Categories',
    component: Categories
  },
  {
    path: '/categories/:category_slug/',
    name: 'Category',
    
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