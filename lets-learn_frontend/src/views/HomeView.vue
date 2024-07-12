<template>
  <div class="bg-gradient-to-r from-fuchsia-400 to-pink-400 mt-1 shadow-sm border border-gray-300 py-8">
    <span class="flex items-center justify-center text-pink-100 text-lg">Welcome to</span>
    <span class="flex items-center justify-center text-pink-100 font-bold text-3xl"> Lets Learn</span>
    <span class="flex items-center justify-center text-pink-100 text-sm">An online intereactive E-learning
      platform</span>

  </div>
  <div class="-mt-1">
    <Carousel :autoplay="3000" :wrap-around="true">
      <Slide v-for="(slideContent, index) in slides" :key="index">
        <div class="w-full flex justify-center items-center min-h-80 bg-gray-50 opacity-90">
          <div class="w-full" v-html="slideContent"></div>
        </div>
      </Slide>

      <template #addons>
        <Navigation />
        <Pagination />
      </template>
    </Carousel>
  </div>
  <div>
    <h1 class="ml-2 text-xl text-rose-800 font-bold flex">
      <BsFire /> &nbsp;Most Popular Courses
    </h1>
    <br>
    <span class="text-gray-500 text-lg ml-2">
      Comming soon
    </span>
  </div>

</template>

<script>
import { Carousel,Navigation,Pagination, Slide } from 'vue3-carousel'
import 'vue3-carousel/dist/carousel.css'
import { BsFire } from '@kalimahapps/vue-icons';
export default {
  name: 'HomeView',
  components: {
    Carousel,
    Slide,
    Navigation,
    Pagination,
    BsFire,

  },
  data() {
    return {
      slides: [
        '<div class="bg-pink-100 py-32 text-pink-800"><div class="text-7xl">&#9885;</div><div><h2 class="text-4xl font-bold">Learning that gets you</h2></div><div> <p>Skills for your present (and your future). Get started with us.</p></div></div>',
        '<div class="bg-sky-100 py-32 text-sky-800"><div class="text-8xl">&#8734;</div><div><h2 class="text-4xl font-bold -mt-4">Learn without limits</h2></div><div> <p>Start, switch, or advance your career with more than 7,000 courses, Professional Certificates, and degrees from world-class universities and companies.</p></div></div>',
        '<div class="bg-gray-100 py-32 text-gray-800"><div class="text-7xl">&#10144;</div><h2 class="text-4xl font-bold">Skills that drive you forward</h2><p>Technology and the world of work change fast — with us, you’re faster. Get the skills to achieve goals and stay competitive.</p></div>',
        
       
        
        // Add more slide contents here
      ]
    };
  },
  mounted() {
    document.title = 'Home | Lets Learn'
  }
}
</script>
<style>

.carousel__slide {
  padding: 10px;
}

.carousel__prev,
.carousel__next {
  box-sizing: content-box;
  border: 5px solid white;
}
</style>