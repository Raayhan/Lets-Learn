<template>
    <div class="text-xl ml-2 p-4 border-l-4 mt-2 bg-violet-50 border-violet-800 text-violet-800 font-medium">
        Categories
    </div>
    <div v-if="$store.state.setIsLoading" class="flex justify-center mt-4">
        <Loading/>
    </div>
    <div class="grid grid-cols-5 gap-4 mt-4 mx-2">
        
            <CategoryBox v-for="category in latestCategories" v-bind:key="category.id" v-bind:category="category"></CategoryBox>
       
    </div>
</template>

<script>
import axios from 'axios'
import CategoryBox from '@/components/CategoryBox'
import Loading from '@/components/Loading'
export default {
    name: 'Categories',
    data() {
        return {
            latestCategories: []
        }
    },
    components: {
        CategoryBox,
        Loading,
    },
    mounted() {
        this.getLatestCategories()
        document.title = 'Categories | Lets Learn'
    },
    methods: {
        async getLatestCategories() {
            this.$store.commit('setIsLoading', true)
            await axios
                .get('api/v1/latest-categories')
                .then(response => { this.latestCategories = response.data })
                .catch(error => {
                    console.log(error)

                })
            this.$store.commit('setIsLoading', false)
        }
    }
}

</script>