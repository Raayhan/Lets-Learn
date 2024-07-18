<template>
    <div class="text-xl ml-2 px-4 py-8 border-l-4 mt-2 bg-violet-50 border-violet-800 text-violet-800 font-medium">
        {{ course.title }}
        <div>
            <span class="text-gray-500 text-sm">{{ course.summary }}</span>
        </div>

    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4">
        <div class="col-span-2 ml-12 text-gray-700 overflow-y-auto overflow-x-hidden max-h-[78vh]" v-html="course.description">


        </div>
        <div class="">
            <figure class="mb-4 flex justify-center">
                <img :src="course.get_image" class="w-96 rounded group-hover:opacity-70 transition-opacity duration-300"
                    alt="Course Thumbnail">
            </figure>
            <span class="text-gray-500 flex justify-center">{{course.title}}</span>

            <div>
                <div class="flex justify-center mt-2">
                    <h3 class="text-green-800 flex text-xs font-medium mr-2 items-center">
                        <BxSolidCategoryAlt /> &nbsp;{{ course.category }}
                    </h3>
                    <h3 class="text-orange-800 text-xs flex font-medium">
                        <CaUserAvatarFilledAlt /> &nbsp;
                        {{ course.author ? course.author.first_name : '' }}{{ course.author ? course.author.last_name :
                        '' }}
                    </h3>
                    <span class="flex ml-2 text-xs">
                        4.5 <svg class="w-3 h-3 ml-1 text-yellow-500 flex items-center" fill="currentColor"
                            viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.286 3.98a1 1 0 00.95.69h4.178c.969 0 1.371 1.24.588 1.81l-3.39 2.48a1 1 0 00-.363 1.118l1.287 3.98c.3.922-.755 1.688-1.54 1.118l-3.39-2.48a1 1 0 00-1.175 0l-3.39 2.48c-.784.57-1.838-.196-1.54-1.118l1.287-3.98a1 1 0 00-.363-1.118l-3.39-2.48c-.783-.57-.38-1.81.588-1.81h4.178a1 1 0 00.95-.69l1.287-3.98z" />
                        </svg>
                    </span>

                </div>
            </div>
            <div class="flex justify-center text-xs text-gray-400 mt-2">
                <span>Published on : {{ formatDate(course.date_added) }}</span>
            </div>
            <div class="flex justify-center mt-6 text-sm">
                <router-link :to="{ name: 'EnrollCourse', params: { category_slug: category_slug, course_slug: course.slug } }"
                    class="rounded bg-violet-800 text-white text-center px-3 w-40 py-2 mr-1 border border-gray-300 hover:bg-violet-900 duration-300">Enroll
                    Now</router-link>
                <button
                    class="rounded bg-rose-700 text-white px-3 w-40 py-2 border border-gray-300 hover:bg-rose-800 duration-300">Report
                    Abuse</button>

            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios'
import DOMPurify from 'dompurify';
import { BxSolidCategoryAlt } from '@kalimahapps/vue-icons';
import { CaUserAvatarFilledAlt } from '@kalimahapps/vue-icons';
import moment from 'moment'

export default {
    name: 'CourseDetails',
    data() {
        return {
            course: {},
            
        }
    },
    components: {
        BxSolidCategoryAlt,
        CaUserAvatarFilledAlt,
       
    },
    mounted() {
        this.getDetails()
    },
    methods: {
        async getDetails() {
            this.$store.commit('setIsLoading', true)
            const category_slug = this.$route.params.category_slug
            const course_slug = this.$route.params.course_slug

            await axios
                .get(`/api/v1/courses/${category_slug}/${course_slug}`)
                .then(response => {
                    this.course = response.data
                    document.title = this.course.title + ' | Lets Learn'
                    
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
            
        },
        formatDate(date) {

            return moment(date).format('DD-MM-YYYY hh:MM A');
        },
    },
    computed: {
        sanitizedDescription() {
            return DOMPurify.sanitize(this.course.description);
        },
    },
}
</script>
