//Hashcode Practice - one pizza
#include <bits/stdc++.h>
using namespace std;

#define vi vector<int> 
#define vvi vector<vi>                                                                                                  

int main() {
    int t;
    cin >> t;

    map<string, int> likes;
    map<string, int> dislikes;

    for (int i = 0; i < t; i++) {
        int n;

        // Likes
        cin >> n;
        for (int j = 0; j < n; j++) {
            string str;
            cin >> str;
            likes[str]++;
        }
        
        // DisLikes
        cin >> n;
        for (int j = 0; j < n; j++) {
            string str;
            cin >> str;
            dislikes[str]++;
        }
        
    }
    
    // Getting all the Item Names
    set<string> items;
    for(auto it = likes.begin();it != likes.end();it++)
    {
        items.insert(it->first);
    }

    for(auto it = dislikes.begin();it != dislikes.end();it++)
    {
        items.insert(it->first);
    }


    vector<string> ans;
    for(auto item:items)
    {
        int score = likes[item] - dislikes[item];

        if(score > 0) {
            ans.push_back(item);
        }
    }
    
    cout<<ans.size();
    for(auto a:ans)
        cout<<" "<<a;
 //   cout<<endl;
    
    return 0;
}