<template>
    <div class="bg-gray-100 border pb-4 rounded group">
        <figure class="mb-4">
            <img :src="category.get_image"
                class="w-full h-60 rounded-t group-hover:opacity-70 transition-opacity duration-300"
                alt="Category Thumbnail">
        </figure>
        <h3 class="text-violet-800 text-xl ml-2 font-medium mb-2">{{ category.name }}</h3>

        <router-link :to="category.get_absolute_url"
            class="mt-4 ml-2 text-sm p-2 bg-violet-800 hover:bg-violet-900 text-white rounded-sm">View Courses</router-link>
    </div>

</template>
<script>
export default {
    name: 'CategoryBox',
    props: {
        category: Object
    }

}
</script>