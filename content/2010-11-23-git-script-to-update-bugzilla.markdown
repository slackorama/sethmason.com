Title: Git script to update Bugzilla
Tags: git, bugzilla


At my work we use [git](http://git-scm.com "Git") and
[Bugzilla](http://www.bugzilla.org "Bugzilla") for source code control and bug
tracking respectively.  We have a process where bugfixes are commited to a
branch off of master with the name of `bugfix/bz1234` where `1234` is the id
of the issue in our bugzilla system.

After a fix is completed, a merge request is filed in our bugzilla system to
merge this branch back into `master` (developers don't have write privileges
to `master`).  We are in the process of writing up a hook to parse commit
messages to automate all of this but it's taking some time.

So, in the interest of making my life a bit easier until then, I took
advantage of Bugzilla's excellent
[email_in.pl](http://www.bugzilla.org/docs/3.0/html/api/email_in.html) to
parse incoming emails to edit tickets and wrote up a command to file fix and
merge tickets for me.

I simply put `git-bz` on my `$PATH` and call it thusly:

    > git bz fix
    > git fix 1.2.3 hotfix | sendmail -t

Note: Our merge tickets require a milestone and a version for the merge ticket, thus
the extra arguments for the merge.

Your system is probably radically different than ours but I thought it'd be
interesting to post something here showing how powerful git is.  Let me know
what you think.


    :::perl
    #!/usr/bin/env perl
    # git-bz -- given a version and target, print out a merge
    #           email for sending to bz

    use warnings;
    use strict;

    use Carp;
    use Git;

    #============================================================================
    # map a shorthand version to the one bz expects for merges
    #============================================================================
    my %versions = (
        'mne'    => 'Merge (M&E/Patch)',
        'rc'     => 'Merge (RC/Major)',
        'hotfix' => 'Merge (Hotfix)'
    );

    #============================================================================
    # get the action and config info
    #============================================================================
    my $action   = shift || '';
    my $bz_email = Git::config('bz.email');

    if (! $bz_email) {
        croak 'No bugzilla email found';
    }

    #============================================================================
    # start doing the work
    #============================================================================
    if ( $action eq 'fix' ) {
        my $user_email = get_user_email();
        my $bz_info = get_bz_info();

        print <<"MAIL";
    To: $bz_email
    From: $user_email
    Subject: Issue $bz_info->{bug} fixed

    \@bug_id = $bz_info->{bug}
    \@bug_status = RESOLVED
    \@resolution = FIXED

    Fixed in $bz_info->{branch} pending merge.

    MAIL

    } elsif ( $action eq 'merge' ) {
        my $target_milestone = shift || '---';
        my $merge_to = shift;
        my $version  = ( $merge_to && $versions{$merge_to} ) ||
                       'unspecified';
        my $bz_info  = get_bz_info();

        my $user_email = get_user_email();

        if ( !defined $bz_info->{bug} ) {
            croak "No bug id found in branch name";
        }

        my $bug_id = $bz_info->{bug};
        my $bz_branch = $bz_info->{branch};

     #============================================================================
     # get the remote branch, url and name
     #============================================================================
        my @remote_info
            = Git::command( 'config', '--get-regexp', '^branch\.'
                            . $bz_branch );
        my ( $remote, $remote_branch );
        for my $line (@remote_info) {
            if ( $line =~ /\.remote\s+(.+)/x ) {
                $remote = $1;
            } elsif ( $line =~ /merge\s+((refs\/)?heads\/)?(.+)/x ) {
                $remote_branch = $3;
            }
        }

        my $remote_url = Git::command_oneline( 'config', '--get-regexp',
            'remote.' . $remote . '.url' );
        if ( $remote_url =~ m/url\s+(.+)/x ) {
            $remote_url = $1;
        }

     #============================================================================
     # get the commits to show
     #============================================================================
        my $commits = Git::command(
            'log',            "$remote/$remote_branch..",
            '--pretty=short', '--name-status'
        );

     #============================================================================
     # finally print out the email message
     #============================================================================
        print <<"MAIL";
    To: $bz_email
    From: $user_email
    Subject: Please merge $bz_branch to $remote_branch

    \@blocked = $bug_id
    \@product = Application Defects
    \@component = Merge Request
    \@version = $version
    \@target_milestone = $target_milestone

    Please merge $bz_branch to the remote branch $remote_branch

    Merge: $bz_branch
    To: $remote_branch
    Repository: $remote_url

    $commits
    MAIL

    } else {
        croak <<"USAGE";
    error: Unknon subcommand: $action
    usage: git bz fix <target>
       or: git bz merge <merge_to> <target>

    USAGE
    }

    #============================================================================
    # get current branch and bug ID
    #============================================================================
    sub get_bz_info {
        my $bz_branch = Git::command_oneline( 'symbolic-ref', 'HEAD' );
        $bz_branch =~ s{^refs\/heads/}{}x;
        my ($bug_id) = $bz_branch =~ m/bz(\d+)/x;
        return { branch => $bz_branch, bug => $bug_id };
    }

    sub get_user_email {
        my $email = Git::command_oneline( 'config', '--get', 'user.email' );
        return $email;
    }

If you want to use it, you'll need to set up a config to point to your own bz
email.

    :::console
    > git config bz.email mybz@somedomain.com

This script is available as a [gist](https://gist.github.com/710374) on [github](http://github.com).
