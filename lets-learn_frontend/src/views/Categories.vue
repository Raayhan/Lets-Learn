<template>
    <div class="text-xl ml-2 p-4 border-l-4 mt-2 bg-violet-50 border-violet-800 text-violet-800 font-medium">
        Categories
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Categories',
    data() {
        return {
            latestCategories: []
        }
    },
    mounted() {
        this.getLatestCategories()
        document.title = 'Categories | Lets Learn'
    },
    methods: {
        async getLatestCategories() {
            //this.$store.commit('setIsLoading', true)
            await axios
                .get('api/v1/latest-categories')
                .then(response => { this.latestCategories = response.data })
                .catch(error => {
                    console.log(error)

                })
            // this.$store.commit('setIsLoading', false)
            console.table(this.latestCategories)
        }
    }
}

</script>