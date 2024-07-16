<template>
    <div class="text-xl ml-2 p-4 border-l-4 mt-2 bg-violet-50 border-violet-800 text-violet-800 font-medium">
        {{ course.title }}

    </div>
    <div class="grid grid-cols-2 gap-4 mt-4">
        <div class="ml-12 text-gray-700 overflow-y-auto overflow-x-hidden max-h-[70vh]" v-html="course.description">


        </div>
        <div class="">
            <figure class="mb-4 flex justify-center">
                <img :src="course.get_image" class="w-96 rounded group-hover:opacity-70 transition-opacity duration-300"
                    alt="Course Thumbnail">
            </figure>
            <span class="text-gray-500 flex justify-center">{{course.title}}</span>
            <div>
                <span class="text-gray-500 text-xs flex justify-center mt-2">{{ course.summary }}</span>
            </div>
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
                </div>
            </div>
            <div class="flex justify-center text-xs text-violet-800 mt-4">
                <span>Published on : {{ formatDate(course.date_added) }}</span>
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
        CaUserAvatarFilledAlt
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

            return moment(date).format('DD/MM/YYYY');
        },
    },
    computed: {
        sanitizedDescription() {
            return DOMPurify.sanitize(this.course.description);
        },
    },
}
</script>
