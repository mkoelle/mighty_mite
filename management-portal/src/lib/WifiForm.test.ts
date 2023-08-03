import {fireEvent, render, screen } from '@testing-library/svelte'
import WifiForm from './WifiForm.svelte'

describe("WifiForm", () => {
    it("renders", async () => {
        // Arrange
        
        // Act
        render(WifiForm)
        // Assert
        const header = await screen.findByText('WiFi connections')
        expect(header).toBeTruthy()
    });
    it("Has a form", async () => {
        // Arrange

        // Act
        render(WifiForm)
        // Assert
        const form = await screen.findByRole('form')
        expect(form).toBeTruthy()
    })
});

