<script lang="ts">
    import { onMount } from "svelte";
    import {
        Label,
        ButtonGroup,
        Dropdown,
        DropdownItem,
        Input,
        Button,
    } from "flowbite-svelte";
    import { Icon } from "flowbite-svelte-icons";
    let networks;

    onMount(async () => {
        await fetch(`http://localhost/networks.json`)
            .then((r) => r.json())
            .then((data) => {
                networks = data;
            });
    });
</script>

<form name="setNetwork" action="#">
    <h2>WiFi connections</h2>

    <ButtonGroup class="w-full">
        <Button
            color="none"
            class="flex-shrink-0 text-gray-900 bg-gray-100 border border-gray-300 dark:border-gray-700 dark:text-white hover:bg-gray-200 focus:ring-gray-300 dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800"
        >
            All Networks<Icon
                name="chevron-down-solid"
                class="w-3 h-3 ml-2 text-white dark:text-white"
            />
        </Button>
        <Dropdown>
            {#if networks}
                {#each networks as network}
                    <ul>
                        <li>
                            <DropdownItem>{network.name}</DropdownItem>
                        </li>
                    </ul>
                {/each}
            {:else}
                <p class="loading">loading...</p>
            {/if}
        </Dropdown>
        <Input placeholder="Network" />
    </ButtonGroup>

    <div class="mb-6">
        <Label for="password" class="mb-2">Password</Label>
        <Input type="password" id="password" placeholder="•••••••••" required />
    </div>
    <br />
    <Button type="submit">Submit</Button>
</form>
