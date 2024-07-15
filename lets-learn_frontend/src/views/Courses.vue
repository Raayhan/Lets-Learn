<template>
    <div class="text-xl ml-2 p-4 border-l-4 mt-2 bg-violet-50 border-violet-800 text-violet-800 font-medium">
        Courses
    </div>
    <div v-if="$store.state.setIsLoading" class="flex justify-center mt-4">
        <Loading />
    </div>
    <div class="grid grid-cols-5 gap-4 mt-4 mx-2">
        <CourseBox v-for="course in latestCourses" v-bind:key="course.id" v-bind:course="course">
        </CourseBox>

    </div>
</template>
<script>

import axios from 'axios'
import CourseBox from '@/components/CourseBox'
import Loading from '@/components/Loading'
export default {
    name: 'Courses',
    data() {
        return {
            latestCourses: []
        }
    },
    components: {
        CourseBox,
        Loading,
    },
    mounted() {
        this.getLatestCourses()
        document.title = 'Courses | Lets Learn'
    },
    methods: {
        async getLatestCourses() {
            this.$store.commit('setIsLoading', true)
            await axios
                .get('api/v1/all-courses')
                .then(response => { this.latestCourses = response.data })
                .catch(error => {
                    console.log(error)

                })
            this.$store.commit('setIsLoading', false)
        }
    }
}

</script>