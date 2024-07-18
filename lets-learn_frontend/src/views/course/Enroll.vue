<template>
    <div class="text-xl ml-2 p-4 border-l-4 mt-2 bg-violet-50 border-violet-800 text-violet-800 font-medium">
        {{ course.title }}
    </div>
    <div class="bg-gray-100 w-2/4 mx-auto mt-6 rounded">
        <div class="flex justify-center text-3xl pt-6 text-green-800 font-bold">
            <SuCheckCircleOutside />
        </div>
        <span class="text-xl text-green-800 font-medium flex justify-center items-center">Confirm Enrollment</span>
<span class="flex justify-center mt-6">You're about to enroll yourself for the following course. Please confirm for your enrollment</span>
        <div class="text-gray-600 mt-6 flex justify-center">
            <span class="ml-4"><b>Course Title :</b> {{ course.title }}</span>

        </div>
        <div class="text-gray-600 flex justify-center">
            <span class="ml-4"><b>Author :</b> {{ course.author ? course.author.first_name : '' }}{{ course.author ?
                course.author.last_name :
                '' }}</span>

        </div>
        <div class="text-gray-600 flex justify-center mb-6">
            <span class="ml-4"><b>Category :</b> {{ course.category }}</span>

        </div>
        <div class="flex justify-center pb-6">
            <button class="bg-green-800 w-40 text-white p-2 rounded hover:bg-green-900 mr-1 font-medium">Yes, I Confirm</button>
            <router-link to="/courses"
                class="bg-gray-800 w-40 text-white text-center p-2 rounded hover:bg-gray-900 font-medium">Cancel</router-link>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { SuCheckCircleOutside } from '@kalimahapps/vue-icons';

export default {
    name: 'Enroll',
    data() {
        return {
            course: {},

        }
    },
    components: {
        SuCheckCircleOutside
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

    },

}
</script>