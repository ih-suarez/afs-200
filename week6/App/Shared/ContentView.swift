//
//  ContentView.swift
//  Shared
//
//  Created by Ismael Suarez on 6/20/21.
//

import SwiftUI

struct ContentView: View {
    @Binding var document: AppDocument

    var body: some View {
        TextEditor(text: $document.text)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView(document: .constant(AppDocument()))
    }
}
