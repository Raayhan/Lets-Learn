<template>
    <div class="text-xl ml-2 p-4 border-l-4 mt-2 bg-violet-50 border-violet-800 text-violet-800 font-medium">
        {{ course.title }}
    </div>
    <div class="bg-gray-100 w-2/4 mx-auto mt-6 rounded">
        <div class="flex justify-center text-3xl pt-6 text-green-800 font-bold">
            <SuCheckCircleOutside />
        </div>
        <span class="text-xl text-green-800 font-medium flex justify-center items-center">Confirm Enrollment</span>
        <span class="flex justify-center mt-6">You're about to enroll yourself for the following course. Please confirm
            for your enrollment</span>
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
            <form @submit.prevent="handleSubmit">
                <button type="submit"
                    :class="{ 'opacity-70 animate-pulse': isSubmitting, 'opacity-100': !isSubmitting, 'opacity-50': errors.length > 0 }"
                    :disabled="errors.length>0"
                    class="bg-green-800 w-40 text-white p-2 rounded hover:bg-green-900 mr-1 font-medium">Yes, I
                    Confirm</button>
            </form>
            <router-link to="/courses"
                class="bg-gray-800 w-40 text-white text-center p-2 rounded hover:bg-gray-900 font-medium">Cancel</router-link>
        </div>
        <div class="" v-if="errors.length">
            <ul v-for="error in errors" v-bind:key="error">
                <li class="bg-red-100 text-red-800 text-sm mb-2 ring-1 ring-red-200 text-center rounded p-2">{{
                    error }}
                </li>
            </ul>

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
            isSubmitting: false,
            errors: []

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
        async handleSubmit() {
            this.isSubmitting = true;

            try {
                const category_slug = this.$route.params.category_slug;
                const course_slug = this.$route.params.course_slug;
                const token = localStorage.getItem('token'); // Adjust based on your auth implementation

                const response = await axios.post(
                    `/api/v1/courses/${category_slug}/${course_slug}/enroll`,
                    {},
                    {
                        headers: {
                            "Content-Type": "application/json",
                            "Authorization": `Token ${token}`
                        }
                    }
                );

                this.$router.push('/dashboard');
            } catch (error) {
                if (error.response) {
                    for (const property in error.response.data) {

                        const errors = error.response.data[property];
                        if (Array.isArray(errors)) {
                            errors.forEach(err => this.errors.push(err));
                        } else {
                            this.errors.push(errors);
                        }
                    }
                } else {
                    this.errors.push('Something went wrong. Please try again later.');
                    console.error('Something went wrong. Please try again later.');
                }
            } finally {
                this.isSubmitting = false;
            }
        },

    },

}
</script>