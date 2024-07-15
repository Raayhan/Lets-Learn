<template>
    <router-link :to="category.get_absolute_url">
        <div class="bg-gray-100 border pb-4 rounded group">
            <figure class="mb-4">
                <img :src="category.get_image"
                    class="w-full h-48 rounded-t group-hover:opacity-70 transition-opacity duration-300"
                    alt="Category Thumbnail">
            </figure>
            <h3 class="text-violet-800 ml-2 font-medium">{{ category.name }}</h3>
            <h3 class="text-gray-500 ml-2 text-xs mb-2">{{ randomNumber }} courses</h3>
        </div>
    </router-link>
</template>
<script>
export default {
    name: 'CategoryBox',
    props: {
        category: Object
    },
    computed: {
        randomNumber() {
            return Math.floor(Math.random() * 100); // Generate a random number between 0 and 99
        }
    }

}
</script>